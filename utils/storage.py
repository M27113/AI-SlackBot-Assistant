import json

def save_conversation(channel_id, user, message, response, file="history.json"):
    try:
        with open(file, "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    history.append({
        "channel": channel_id,
        "user": user,
        "message": message,
        "response": response
    })

    with open(file, "w") as f:
        json.dump(history, f, indent=4)
