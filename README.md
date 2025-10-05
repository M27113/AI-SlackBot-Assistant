# 🤖 AI-SlackBot-Assistant 🪄| Your Smart Workspace Bot
⚡ Boost Slack productivity with an AI bot that answers, summarizes, and plans your tasks.

## 📖 Project Overview

**AI-SlackBot-Assistant** is a **smart, context-aware AI bot** designed for Slack workspaces.  
It can interact with users via **channel mentions** and **direct messages**, providing:  

- 📨**Direct Messages:** Real-time responses to greetings, questions, and commands.  
- 📢 **Channel Mentions:** Public answers, summaries, and guidance within channels.  
- 📚 Summaries of articles, movies, anime plots, or any text input.  
- 🧠 Intelligent task planning and daily schedule suggestions.  
- 🎯 Motivational quotes and guidance for users.  
- 🔗 Modular design to easily add new AI features or integrations.  

Built using **Python**, **Slack Bolt with Socket Mode**, and **OpenAI GPT**, this bot is ideal for showcasing AI-powered productivity in messaging platforms.

---

## 🛠 Tech Stack

- 🟢 **Python** for Slack integration  
- 🟣 **OpenAI GPT** for AI reasoning & responses  
- ⚡ **Slack API (Socket Mode)** for real-time events  

---

## 📂 Project Structure

    ai-slackbot-assistant/
    ├── .env                           # Stores API keys, tokens
    ├── main.py                        # Entry point: Slack event handling & bot setup
    ├── ai_handler.py                  # Handles communication with OpenAI API
    ├── features/                      # Modular AI features
    │     ├── summarizer.py            # Summarizes text, articles, anime, movies
    │     ├── planner.py               # Plans tasks, schedules, and study sessions
    │     └── quotes.py                # Generates motivational quotes
    ├── utils/
    │     └── storage.py               # Optional: logs messages, responses, timestamps
    ├── demo/                          # Screenshots for README/demo
    └── requirements.txt               # Python dependencies

## 🏗 Architecture

    +---------------+    +----------------+    +-----------------+    +-----------------+    +----------------+
    | User Input    |--->| Slack Event    |--->| AI Handler      |--->| OpenAI GPT      |--->| Slack Reply    |
    | (Channel/DM)  |    | (mention/DM)   |    | ai_handler.py   |    | ai_handler.py   |    | Channel / DM   |
    +---------------+    +----------------+    +-----------------+    +-----------------+    +----------------+

### 📝 Explanation

- **User Input:** Messages from Slack users (channel mentions or DMs).  
- **Slack Event:** Captures events using Socket Mode (`app_mention` or `message`).  
- **AI Handler:** Processes Slack events, prepares input for GPT, and determines the response.  
- **OpenAI GPT API:** Generates context-aware responses using the GPT model.  
- **Slack Reply:** Sends the final response back to the channel or DM.  

---


## ⚡ Installation & Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/M27113/AI-SlackBot-Assistant.git
    cd AI-SlackBot-Assistant

2. Create virtual environment & activate
     ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate


3. Install dependencies
    ```bash
    pip install -r requirements.txt


4. Create .env file
    ```bash
    SLACK_BOT_TOKEN=xoxb-your-bot-token
    SLACK_APP_TOKEN=xapp-your-app-token
    OPENAI_API_KEY=your-openai-api-key


5. Run the bot
    ```bash
    python main.py


**Note**: 
- ⚠️ Ensure your Slack app has the following Bot Token Scopes:
  - app_mentions:read, chat:write, im:write
- Also subscribe to Bot Events: app_mention and message.im

## 💻 Usage

### 💬 Channel Mentions

1. Invite the bot to a channel:
    ```bash
    /invite @MyBot


2. Mention the bot:
    ```bash
    @MyBot Hello there!

    - The bot replies in the same channel.

### 📨 Direct Messages

1. Open a DM with the bot via **Apps → MyBot → Message**

  ![DM](/demo/bot.png) 

2. Type a message:
    ```bash
    Hello AI!

    - The bot replies directly in the DM.
  
---
## 🎬 Demo / Output

### App in Action – 📨 Direct Messages

### 💬 Chat with the Bot

Open a direct message with the bot in Slack and see it respond in real-time:

- *Bot summarizing the "Haikyuu" anime plot in a DM.*

![DM Haikyuu Summary](/demo/haikyu.png)  

- *Bot giving 3 book recommendations on data science in a DM.*

![DM Data Science Books](/demo/books.png)  

- *Bot planning a 2-hour study session for the user.*

![DM Study Plan](/demo/study.png) 

### 📢 Channel Mentions 

- *Bot suggesting a quick workout routine in a Slack channel.*

![Channel Quick Workout](/demo/workout.png)  

- *Bot summarizing "Avengers: Endgame" movie plot in the channel.*

![Channel Endgame Summary](/demo/endgame.png)  

- *Bot explaining reinforcement learning in simple terms in response to a user query in the channel.*

![Channel Reinforcement Learning](/demo/rein_lear.png)


### 🖥 Terminal Output

## 🧪 Test Queries

| Context      | Input                                            | Expected Response                                                      |
|--------------|--------------------------------------------------|------------------------------------------------------------------------|
| Channel      | `Suggest a quick workout routine.`               | A simple workout plan with exercises for warm-up, cardio, and cool-down|
| Channel      | `Summarize "Avengers: Endgame" movie plot.`      | A concise summary covering the main story of "Avengers: Endgame"       |
| Channel      | `Explain reinforcement learning in simple terms.`| A short explanation of reinforcement learning                          |
| Direct Msg   | `Summarize the plot of "Haikyu" anime.`          | A brief summary of "Haikyu!" anime plot focusing on the main characters|
| Direct Msg   | `Give me 3 book recommendations on data science.`| A list of 3 popular data science books with short descriptions         |
| Direct Msg   | `Plan a 2-hour study session for today.`         | A suggested 2-hour study plan with time allocation for each topic      |

- Screenshots for each test query are included in the `demo/` folder.
---

## ✍️ Contributing
- Fork the repo, create a branch, implement features, and submit a pull request.  
- Ensure all changes are tested in a Slack workspace.  
- Add proper logging and error handling for new features.

---

## 🔮 Future Work

- Add interactive Slack buttons & modals for richer user interactions.

- Integrate multi-turn conversation context.

- Deploy on cloud for 24/7 availability.

- Add more AI features like summarizing PDFs, emails, and docs.
