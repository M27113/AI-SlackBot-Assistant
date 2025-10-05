import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
# Initialize OpenAI client using API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ------------------------------
# 🔮 AI Response Function
# ------------------------------
def get_ai_response(prompt: str) -> str:
    """
    Generates a conversational AI response using OpenAI's GPT model.
    """
    try:
        # Use the latest GPT-4 or GPT-3.5-turbo model depending on your plan
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # small + fast model ideal for chatbots
            messages=[
                {"role": "system", "content": "You are SlackSage 🪄, a friendly and intelligent Slack assistant who helps with work automation, coding, and AI queries."},
                {"role": "user", "content": prompt},
            ],
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print(f"❌ Error from OpenAI API: {e}")
        return "⚠️ Sorry, I couldn’t generate a response right now. Please try again."
