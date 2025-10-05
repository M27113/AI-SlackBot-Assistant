import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from ai_handler import get_ai_response
from dotenv import load_dotenv
import logging

# Setup logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

load_dotenv()

# ------------------------------
# ⚙️ Load environment variables
# ------------------------------
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

if not SLACK_BOT_TOKEN or not SLACK_APP_TOKEN:
    raise ValueError("❌ Missing Slack tokens. Check your .env file.")

# ------------------------------
# 🚀 Initialize Slack app
# ------------------------------
app = App(token=SLACK_BOT_TOKEN)


# ------------------------------
# 💬 Handle mentions (@SlackSage)
# ------------------------------
@app.event("app_mention")
def handle_mention(body, say, logger):
    event = body.get("event", {})
    text = event.get("text", "")

    logger.info(f"📢 Mention detected: {text}")
    try:
        response = get_ai_response(text)
        say(response)
    except Exception as e:
        logger.error(f"Error in handle_mention: {e}")
        say("⚠️ Oops! Something went wrong while processing your request.")


# ------------------------------
# 💌 Handle direct messages (DMs)
# ------------------------------
@app.event("message")
def handle_dm(event, say):
    if event.get("channel_type") == "im":
        user = event.get("user")
        text = event.get("text", "")
        if user and text:
            response = get_ai_response(text)
            say(text=response)

    # Ignore system or bot messages
    if not user or user == "USLACKBOT":
        return

    logger.info(f"💬 Direct Message from {user}: {text}")
    try:
        response = get_ai_response(text)
        say(response)
    except Exception as e:
        logger.error(f"Error in handle_dm: {e}")
        say("⚠️ Sorry, I ran into an issue while responding!")


# ------------------------------
# 🏁 Start the app
# ------------------------------
if __name__ == "__main__":
    print("⚡️ Slack AI Agent starting...")
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
