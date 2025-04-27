from fastapi import FastAPI, Depends
from pydantic import BaseModel
import openai
import os
import json
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Load FAQ data
with open("faqs.json", "r") as f:
    faq_data = json.load(f)

# Set up SQLite database
DATABASE_URL = "sqlite:///./chatbot.db"

# Database setup using SQLAlchemy
Base = declarative_base()

# Define the ConversationHistory model
class ConversationHistory(Base):
    __tablename__ = "conversation_history"
    
    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, index=True)
    response = Column(String)
    role = Column(String)

# Set up the database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Define the Question model
class Question(BaseModel):
    query: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def save_conversation(db, query, response, role):
    db_conversation = ConversationHistory(query=query, response=response, role=role)
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation

def find_answer(query, db):
    # List of general conversational responses
    general_responses = {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! How can I help you?",
        "how are you": "I'm doing great, thank you for asking! How about you?",
        "what's your name": "I'm an FAQ chatbot, here to help you!",
        "introduce yourself": "I'm a chatbot designed to assist with frequently asked questions. How can I help you today?"
    }

    query_lower = query.lower()

    # Check if query matches any FAQ exactly
    for faq in faq_data:
        if query_lower == faq["question"].lower():  # Exact match for FAQ question
            save_conversation(db, query, faq["answer"], "assistant")
            return faq["answer"]
    
    # If not found in FAQ, check for general conversational statements
    for key, response in general_responses.items():
        if query_lower == key:  # Only exact match for general statements
            save_conversation(db, query, response, "assistant")
            return response

    # If not found in FAQs or general responses, ask OpenAI with conversation history for context
    try:
        # Retrieve previous conversation history
        conversation_history = []
        conversations = db.query(ConversationHistory).all()
        for convo in conversations:
            conversation_history.append({"role": convo.role, "content": convo.query if convo.role == "user" else convo.response})
        
        # Add the user's query to the conversation history
        conversation_history.append({"role": "user", "content": query})
        
        # Ask OpenAI with conversation context
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful FAQ chatbot."}] + conversation_history
        )
        
        answer = response["choices"][0]["message"]["content"]
        
        # Save the conversation to the database
        save_conversation(db, query, answer, "assistant")
        
        return answer
    except Exception as e:
        return "Sorry, I couldn't fetch an answer at the moment."

@app.post("/ask")
async def ask_question(question: Question, db: Session = Depends(get_db)):
    answer = find_answer(question.query, db)
    return {"answer": answer}