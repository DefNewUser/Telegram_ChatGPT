import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY_GPT")

# telegram_api_key = os.environ['TELEGRAM_API_KEY_GPT']

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Привет, как дела?",
    temperature=0.9,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
)

print(response['choices'][0]['text'])