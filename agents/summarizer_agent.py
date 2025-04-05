from langchain.llms import Ollama

llm = Ollama(model="mistral:instruct")

def summarize_ticket(text):
    prompt = f"Summarize this support ticket:\n{text}"
    return llm(prompt)
