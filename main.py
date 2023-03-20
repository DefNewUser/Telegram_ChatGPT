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

# Create a dictionary to store the conversation history of each user
user_history = {}

# Handle the "/clear" command
@bot.message_handler(commands=['clear'])
def handle_clear(message):
    user_id = message.from_user.id
    
    # Clear the user's conversation history
    user_history[user_id] = ""
    
    # Send a message to the user to indicate the start of a new chat
    bot.send_message(chat_id=message.chat.id, text="Let's start a new chat! Send me a message.")

# Handle incoming messages with OpenAI
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    
    # Retrieve the user's conversation history from memory
    history = user_history.get(user_id, "")
    prompt = history + message.text
    
    # Generate response using OpenAI
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    
    # Store the current message in the user's conversation history
    user_history[user_id] = prompt + response.choices[0].text
    
    # Send response back to user
    bot.send_message(chat_id=message.chat.id, text=response.choices[0].text)

# Start the bot
bot.polling()



#------------------------------------------------------------
# import os
# import openai
# import telebot
# from dotenv import load_dotenv

# # Initialize the OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY_GPT")

# # Initialize the Telebot API key

# load_dotenv()
# telegram_api_key = os.getenv("TELERGAM_API_KEY_GPT")

# bot = telebot.TeleBot(telegram_api_key)


# # Handle incoming messages with OpenAI
# @bot.message_handler(func=lambda _: True)
# def handle_message(message):
#     # Generate response using OpenAI
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=message.text,
#         temperature=0.5,
#         max_tokens=3000,
#         top_p=1,
#         frequency_penalty=0.0,
#         presence_penalty=0.6,
#     )
#     # Send response back to user
#     bot.send_message(chat_id=message.chat.id, text=response.choices[0].text)

# # Start the bot
# bot.polling()


