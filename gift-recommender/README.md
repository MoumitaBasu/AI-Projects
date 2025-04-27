
# E-commerce Gift Recommendation System

## Overview
This project leverages AI models and web scraping to provide personalized gift recommendations based on user preferences. The system uses a combination of large language models (LLMs) like **Gemma**/ **Phi-2** via **Ollama**, **GPT4All**, and **Mistral** for query generation and **web scraping** (using SerpAPI) to fetch the most relevant e-commerce product links from sites like **Amazon**, **Flipkart**, **Etsy**, and more.

## Features
- **Personalized Gift Suggestions**: Tailored recommendations based on user input, such as interests, lifestyle, and budget.
- **Web Scraping Integration**: Fetches real-time product links from trusted e-commerce platforms.
- **AI-powered Query Structuring**: Uses language models to create accurate search queries for gift retrieval.
- **Fast Response Time**: Optimized AI and scraping methods for a quick and responsive experience.

## Requirements
Ensure you have the following Python libraries installed:
- **streamlit**: For web interface
- **langchain_community**: For using Ollama and other LLMs
- **torch**: For running machine learning models locally
- **requests**: For web scraping
- **beautifulsoup4**: For parsing HTML
- **googlesearch-python**: For searching via Google
- **textblob**: For sentiment analysis (optional)
- **serpapi**: For search API (optional)
- **yaml**: For managing configurations (optional)

Install dependencies via `pip`:
```bash
pip install -r requirements.txt
```

## How to Use
1. **Run the Streamlit app**:
   Launch the application using the command:
   ```bash
   streamlit run app.py
   ```
2. **Interact with the Web Interface**:
   - Select the recipient, occasion, and preferences.
   - Input the budget and any additional details like color preferences, personality, and lifestyle.
   - Choose the method for finding gifts (Web Scraping, Local AI Model, etc.)
   - Click **Find Gift Suggestions** to receive personalized product links and details.

## Model Options
You can choose between various AI models for generating the gift suggestion queries:
- **Mistral (Hugging Face)**: Uses the Mistral-7B model for generating search queries.
- **Ollama (Gemma/Phi-2)**: A fast and efficient local AI model option.
- **GPT4All**: A model specifically trained to generate creative responses with minimal latency.

## Example Usage
```python
query = (
    f"Buy {gift_type} gift for {recipient}, "
    f"perfect for {lifestyle} lifestyle, "
    f"great for someone who loves {', '.join(interests) if interests else 'various interests'}, "
    f"aligned with {', '.join(values) if values else 'diverse'} values, "
    f"favorite color {color}. "
    f"Looking for {fav_things if fav_things else 'top-rated brands'}. "
    f"Budget: ${budget[0]} - ${budget[1]}. "
    f"Fast shipping available. "
    f"site:{' OR site:'.join(ecommerce_sites)}"
)
```

## Notes
- Ensure that the model (Ollama, GPT4All, etc.) is correctly installed on your local machine. You might need to configure the path to the model or download it if it's not yet installed.
- Web scraping may be slow depending on the external website's response time and the number of results being processed.
  
## Future Improvements
- **Caching**: Add caching for frequent searches to improve performance.
- **Sentiment Analysis**: Integrate sentiment analysis for better filtering of high-quality products.
- **UI Enhancements**: Improve user experience and responsiveness with more dynamic visual components.

## Contributing
Feel free to fork this repository, submit issues, or create pull requests. All contributions are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
