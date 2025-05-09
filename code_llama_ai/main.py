from ai_engine.llama_interface import LlamaInterface
from prompts import get_prompt

def main():
    question = input("Enter your question: ")
    prompt = get_prompt("default", question=question)
    llm = LlamaInterface()
    response = llm.generate_response(prompt)
    print("AI Response:", response)

if __name__ == "__main__":
    main() 