
# Document Q&A Bot with Streamlit, LangChain, HuggingFace, and OpenAI

This is an intelligent Document Q&A Bot that allows users to upload documents (PDF or DOCX) and interact with the content via questions and answers. It supports both **OpenAI** and **local HuggingFace models** for Question-Answering (QA), with optional **voice input** and **extracted table visualization**.

## 🛠️ Tech Stack

- **Streamlit**: For building the web interface
- **LangChain**: For document processing and question answering
- **OpenAI API**: For QA with OpenAI models (e.g., GPT-3.5, GPT-4)
- **HuggingFace**: For running local models for QA
- **SpeechRecognition**: For converting voice input to text
- **pdfplumber**: For extracting tables from PDF files
- **FAISS**: For efficient semantic search and vector storage

## 🚀 Features

- **Document Upload**: Upload PDF or DOCX files.
- **Text and Voice QA**: Ask questions based on the document's content.
- **Local Model Support**: Choose between OpenAI API or a HuggingFace local model.
- **File Upload History**: View previously uploaded files.
- **Conversation History**: Keep track of previous Q&A sessions.
- **Extracted Table Visualization**: Extract and display tables from PDF documents.
- **User Authentication**: Secure access with basic authentication.

## 🏁 Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/your-username/Document-QA-Bot.git
cd Document-QA-Bot
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your OpenAI API Key

Create an `.env` file at the root of the project and add your OpenAI API key:

```text
OPENAI_API_KEY=your-openai-api-key
```

### 5. Run the Streamlit app

```bash
streamlit run app.py
```

This will start the app at `http://localhost:8501` where you can interact with the Document Q&A Bot.

## 📝 How to Use

1. **Authentication**: 
   - Log in using the **username**: `admin` and **password**: `secret`.

2. **Upload a Document**: 
   - Choose a PDF or DOCX file to upload from the sidebar.
   - The document will be processed, and you can start asking questions based on its content.

3. **Ask Questions**:
   - You can type your question in the **text input** or use **voice input** (via a WAV or MP3 file) for speech-to-text recognition.

4. **Switch Between OpenAI and HuggingFace Models**:
   - Use the sidebar to choose between **OpenAI models** or a **local HuggingFace model** for question-answering.

5. **Extracted Tables**: 
   - If the uploaded document contains tables, they will be displayed under the **Extracted Tables** section.

6. **History**:
   - View previously uploaded files and the conversation history from the sidebar.

## ⚙️ Configuration Options

- **Choose Model**: 
  - Switch between OpenAI or HuggingFace models for QA processing.
  
- **OpenAI API Key**: 
  - Enter your OpenAI API key to use OpenAI models for question answering.

## 🧪 Optional Enhancements

You can add the following features later:

- **File Upload History**: Track and visualize all previously uploaded files.
- **Speech-to-Text**: Implement speech-to-text for question input.
- **Table Visualization**: Automatically extract and visualize tables from documents.
- **User Authentication**: Implement more advanced user authentication and token management.

## 📦 Dependencies

- **streamlit**
- **langchain**
- **openai**
- **transformers**
- **faiss-cpu**
- **sentence-transformers**
- **pdfplumber**
- **speechrecognition**

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- **Streamlit** for building amazing web apps for machine learning.
- **LangChain** for making it easy to integrate with large language models.
- **OpenAI** for providing powerful language models like GPT-3 and GPT-4.
- **HuggingFace** for making local LLMs available.
- **SpeechRecognition** for enabling voice input.
