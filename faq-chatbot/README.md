# FAQ Chatbot with OpenAI and FastApi
This project implements an FAQ chatbot that leverages OpenAI's GPT-3.5 API to provide conversational answers to both frequently asked questions (FAQs) and general user queries. The chatbot also stores conversation history in an SQLite database to improve contextual responses.

## Features:
- NLP-enhanced FAQ matching: User queries are preprocessed and semantically matched against a predefined FAQ dataset using sentence embeddings (e.g., sentence-transformers) for fast and accurate responses without always calling GPT.

- Intent classification: Basic NLP models classify user intent (e.g., greeting, info request, help) to determine how to respond — whether to use a canned response, FAQ, or pass to GPT.

- General conversation handling: Leverages OpenAI GPT-3.5 for more complex or open-ended queries with conversation context.

- Conversation memory: Stores chat history in an SQLite database to maintain context across turns.

- Preprocessing pipeline: User inputs are cleaned, normalized, and optionally corrected using standard NLP techniques (tokenization, lemmatization, etc.) before matching or sending to GPT.

- Dockerized: Fully containerized setup for easy deployment on any platform.

## Tech Stack:
 - Backend: FastAPI, OpenAI API
 - Database: SQLite (SQLAlchemy ORM)
 - Containerization: Docker
 - Frontend: (Can be added, e.g., Streamlit, if you want to provide a UI for users)

## Requirements:
- Python 3.7+
- Docker
- Docker Compose (if needed)
- NLP Models: sentence-transformers, spaCy

## Setup Instructions:
1. Clone the repository:
```bash
git clone https://github.com/your-username/faq-chatbot.git
```
2. Install dependencies:

 - Option 1: Using Docker (Recommended)
 
   - This project is dockerized for easy deployment.
   
   - Build the Docker container:

   ```bash
   docker-compose build
   ```
   - Start the application:

   ```bash
   docker-compose up
   ```
 
 - Option 2: Local Development (Without Docker)
 
   - Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```
   
   - Activate the virtual environment:
   
    - On Windows:
  
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```
   
   - Install dependencies:

   ```bash
   pip install -r frontend/requirements.txt
   ```
   ```bash
   pip install -r backend/requirements.txt
   ```
   
   - Set up your .env file (create one in the root directory):
   OPENAI_API_KEY=your-openai-api-key
   
   - Start the application:

   ```bash
   uvicorn main:app --reload
   ```

## 3. Application URL:
Once the server is up, the API will be running at http://127.0.0.1:8000

You can interact with the API by sending POST requests to the /ask endpoint with a query as the payload.

Example request:

json
{
  "query": "What is your name?"
}
Response:
{
  "answer": "I am an FAQ chatbot here to assist you with common questions."
}

## NLP Pipeline & Intelligence:
FAQ Matching: User queries are semantically matched against faqs.json using vector embeddings for high-accuracy lookup.

Intent Detection: NLP classifies whether the message is a greeting, question, or fallback.

Text Preprocessing: Stop-word removal, lemmatization, normalization.

Sentiment & Entity Extraction (optional): For enhancing response tone or personalization.

Contextual GPT: GPT is used when no FAQ match is found, with recent conversation history sent as context.

## Database:
The project uses SQLite to store conversation history. The table conversation_history contains the following columns:

 - id: Auto-incrementing primary key.
 - query: The user's input.
 - response: The chatbot's response.
 - role: The role of the speaker (either "user" or "assistant").

To initialize the database, the project automatically creates the necessary tables upon startup. You can inspect the database using SQLite tools or SQLite browser.

## FAQ:
Q1: How do I interact with the chatbot?

You can send POST requests to the /ask endpoint of the API. The request body should contain a query key with the user's question or statement.

Q2: Does the chatbot remember previous conversations?

Yes, the chatbot saves the conversation history in an SQLite database. This history is used to provide better context in the chatbot’s responses.

Q3: Can I add more FAQs?

Yes! You can easily add more FAQ data by editing the faqs.json file in the root directory. The chatbot will automatically load this data at startup.

Q4: How can I deploy this chatbot to production?

Since the application is dockerized, you can deploy it on any platform that supports Docker. You can use platforms like Heroku, AWS, or DigitalOcean to host the container.

Q5: How does the chatbot handle general conversation?

The chatbot is designed to understand and respond to general statements like greetings or personal introductions. These responses are defined in the general_responses dictionary in the backend.
