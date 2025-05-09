import requests
import json

def test_code_generation():
    url = "http://localhost:8000/query"
    
    # Code generation requirements
    payload = {
        "query": "Generate a Python function to implement a binary search algorithm with detailed comments.",
        "requirements": [
            "The function must handle both ascending and descending sorted arrays",
            "Should include type hints for better code clarity",
            "Must include edge cases handling (empty array, single element)",
            "Should have detailed docstring explaining parameters and return value",
            "Must include example usage in the docstring",
            "Should be optimized for time complexity O(log n)"
        ]
    }
    
    try:
        print("\nTesting Code Generation Requirements...")
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Response from MCP server:")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Error: {e}")

def test_code_explanation():
    url = "http://localhost:8000/query"
    
    # Code explanation requirements
    payload = {
        "query": "Explain this code and suggest improvements:\n```python\ndef process_data(data):\n    result = []\n    for item in data:\n        if item > 0:\n            result.append(item * 2)\n    return result\n```",
        "requirements": [
            "Must explain the code's purpose and functionality",
            "Should identify potential performance issues",
            "Must suggest at least two improvements",
            "Should include example of improved code",
            "Must explain why the improvements are better",
            "Should consider edge cases and error handling"
        ]
    }
    
    try:
        print("\nTesting Code Explanation Requirements...")
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Response from MCP server:")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Error: {e}")

def test_debugging_help():
    url = "http://localhost:8000/query"
    
    # Debugging help requirements
    payload = {
        "query": "Help me debug this error: 'TypeError: unsupported operand type(s) for +: 'int' and 'str'' in the following code:\n```python\ndef calculate_total(items):\n    total = 0\n    for item in items:\n        total += item['price']\n    return total\n```",
        "requirements": [
            "Must explain the cause of the error",
            "Should provide a fixed version of the code",
            "Must explain why the error occurred",
            "Should suggest ways to prevent similar errors",
            "Must include input validation",
            "Should add error handling for edge cases"
        ]
    }
    
    try:
        print("\nTesting Debugging Help Requirements...")
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Response from MCP server:")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Starting MCP Server Tests for Code-Related Queries...")
    test_code_generation()
    test_code_explanation()
    test_debugging_help() 