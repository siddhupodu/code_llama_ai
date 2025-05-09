# Code Llama AI - VS Code Plugin Backend

This project implements a Model Context Protocol (MCP) server that serves as the backend for a VS Code plugin, enabling AI-powered code assistance using CodeLlama through Ollama.

## Project Structure
```
code_llama_ai/
├── ai_engine/
│   ├── __init__.py
│   └── llama_interface.py     # Core LLM communication logic
├── mcp_server.py              # FastAPI server implementation
├── test_mcp.py               # Test cases for the MCP server
├── main.py                   # Simple CLI test interface
├── prompts.py                # Prompt templates
└── requirements.txt          # Project dependencies
```

## Prerequisites

1. **Python 3.9+**
2. **Ollama** installed and running
   - Download from: https://ollama.ai/
   - Install and run: `ollama serve`
3. **CodeLlama Model**
   - Pull the model: `ollama pull codellama`

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd code_llama_ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Code

### 1. Start Ollama
```bash
ollama serve
```

### 2. Start the MCP Server
```bash
uvicorn mcp_server:app --reload
```
The server will run at `http://localhost:8000`

### 3. Run Tests
```bash
python test_mcp.py
```

## How It Works

### 1. MCP Server (mcp_server.py)
- FastAPI-based server that handles code-related queries
- Accepts POST requests at `/query` endpoint
- Combines requirements and queries into structured prompts
- Communicates with CodeLlama through Ollama

### 2. LlamaInterface (ai_engine/llama_interface.py)
- Handles communication with Ollama
- Manages prompt formatting and response parsing
- Includes error handling and timeout management

### 3. Test Cases (test_mcp.py)
Three main test scenarios:
1. **Code Generation**
   - Generates code based on requirements
   - Example: Binary search algorithm implementation

2. **Code Explanation**
   - Explains and improves existing code
   - Provides suggestions and best practices

3. **Debugging Help**
   - Helps debug code errors
   - Provides fixes and prevention strategies

## Testing the API

### Using curl
```bash
curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d '{
       "query": "Generate a Python function to implement a binary search algorithm",
       "requirements": [
         "The function must handle both ascending and descending sorted arrays",
         "Should include type hints for better code clarity"
       ]
     }'
```

### Using Python
```python
import requests

response = requests.post(
    "http://localhost:8000/query",
    json={
        "query": "Your question here",
        "requirements": ["Your requirements here"]
    }
)
print(response.json())
```

## Common Issues and Solutions

1. **Ollama Connection Timeout**
   - Ensure Ollama is running: `ollama serve`
   - Check if CodeLlama is pulled: `ollama pull codellama`
   - Increase timeout in `llama_interface.py` if needed

2. **Module Not Found Errors**
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - Check Python environment

3. **Server Not Starting**
   - Ensure port 8000 is available
   - Check if FastAPI and uvicorn are installed

## Next Steps

1. **VS Code Plugin Integration**
   - Create VS Code extension
   - Implement API communication
   - Add UI components

2. **Enhanced Features**
   - Add more code analysis capabilities
   - Implement context-aware suggestions
   - Add support for multiple programming languages

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
[Add your license information here] 