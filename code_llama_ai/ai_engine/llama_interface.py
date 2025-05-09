import requests

class LlamaInterface:
    def __init__(self, model_name="codellama", ollama_url="http://localhost:11434/api/generate"):
        self.model_name = model_name
        self.ollama_url = ollama_url

    def generate_response(self, prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }
        try:
            print("Sending request to Ollama...")
            response = requests.post(self.ollama_url, json=payload, timeout=500)
            print("Received response from Ollama.")
            response.raise_for_status()
            data = response.json()
            return data.get("response", "[No response from model]")
        except Exception as e:
            return f"[Error communicating with Ollama: {e}]" 