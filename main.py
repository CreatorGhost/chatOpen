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


def language_assistant(message):
    response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                    "role": "system",
                    "content": "You are very knowlegeble ai who have waste knowledge about Hindi languages as well as English and you work as a language translator to traslate from English to Hindi"
                    },
                    {
                        "role": "user",
                        "content": f" Translate the following message : {message}"
                    }
                ]
                )
    return response["choices"][0]["message"]["content"]



message = "Hello welcome and thanks for the help"
resposne = language_assistant(message)

print(resposne)