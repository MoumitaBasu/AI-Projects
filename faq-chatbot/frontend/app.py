import streamlit as st
import requests

st.title("🤖 FAQ Chatbot")

st.write("Ask me anything!")

user_input = st.text_input("Your question:")

if st.button("Ask"):
    if user_input:
        try:
            # Send POST request to FastAPI
            response = requests.post("http://backend:8000/ask", json={"query": user_input}) # Chane to http://127.0.0.1:8000/ask for running in local
            
            # Check if the response is valid and JSON
            if response.status_code == 200:
                answer = response.json().get("answer", "Sorry, I couldn't find an answer.")
            else:
                answer = f"Error: {response.status_code}, {response.text}"

        except requests.exceptions.RequestException as e:
            # If there is any issue with the request, show an error message
            answer = f"Request failed: {e}"

        st.write(f"**Chatbot:** {answer}")
    else:
        st.warning("Please enter a question.")
