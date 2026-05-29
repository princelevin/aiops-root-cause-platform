import requests


# Local Ollama endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# LLM model used for analysis
MODEL_NAME = "llama3.2"


def ask_ollama(prompt: str):
    """
    Send prompt to local Ollama model.
    """

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
    }

    try:
        # Call Ollama API
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        # Return generated response
        return data.get("response", "").strip()

    except requests.exceptions.RequestException as error:
        # Return error message if Ollama is unavailable
        return f"Ollama error: {str(error)}"