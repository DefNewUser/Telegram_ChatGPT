import os
import openai
import telebot
from dotenv import load_dotenv

# Initialize the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY_GPT")

# Initialize the Telebot API key

load_dotenv()
telegram_api_key = os.getenv("TELERGAM_API_KEY_GPT")

bot = telebot.TeleBot(telegram_api_key)

# Handle incoming messages with OpenAI
@bot.message_handler(func=lambda _: True)
def handle_message(message):
    # Generate response using OpenAI
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    # Send response back to user
    bot.send_message(chat_id=message.chat.id, text=response.choices[0].text)

# Start the bot
bot.polling()



