import os
import openai
from dotenv import load_dotenv
from pprint import pprint as print
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']


def generate_artile(tile):
    response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                    "role": "system",
                    "content": "You are very knowlegeble ai that helps people on witing new artile and you artile follows all the good practices"
                    },
                    {
                        "role": "user",
                        "content": f"Write an artile about {tile}"
                    }
                ]
                )
    return response["choices"][0]["message"]["content"]



title = "2008 Market Crash Report"

res = generate_artile(title)

print(res)
