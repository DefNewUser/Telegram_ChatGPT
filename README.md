## This code is used to create a chatbot in Telegram that will use the OpenAI API to generate responses to incoming messages.

# Installation
1. Add your own data `TELERGAM_API_KEY_GPT`, `OPENAI_API_KEY_GPT` and `ALLOWED_USERS`
2. Install all the necessary components: 
```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```

The bot in operation uses a SQLite database as a cold store of submitted data, to provide context for 
ChatGPT's queries, and to make these queries more relaxed.