from langchain_community.llms import Ollama

def generate_gift_suggestions(query, model_type="mistral", max_length=150, timeout=10):
    """
    Generates gift suggestions using a local Ollama model.
    
    - model_type: "mistral" (default), "gemma", "llama2", etc.
    - max_length: Limits response length for speed.
    - timeout: Prevents long wait times.
    """
    try:
        llm = Ollama(
            model=model_type,
            temperature=0.5,  # Balance between creativity and relevance
            num_ctx=2048  # Optimize context size for faster inference
        )

        response = llm.invoke(query, max_tokens=max_length)
        return response.strip()  # Clean output
    except Exception as e:
        return f"Error: {e}. Ensure Ollama is installed and model is available."