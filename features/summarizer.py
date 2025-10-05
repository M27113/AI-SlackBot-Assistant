from ai_handler import get_ai_response

def summarize_text(text):
    prompt = f"Summarize the following text in short bullet points:\n{text}"
    return get_ai_response(prompt)
