import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY is not set. Add it to a .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model='openai/gpt-oss-120b',
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Write a poem about the beauty of nature."
        }
    ]
)

print(response.choices[0].message.content)
