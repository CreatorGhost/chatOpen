import os
import openai
from dotenv import load_dotenv

load_dotenv()



# print(os.environ['OPENAI_API_KEY'])


# openai.api_key = os.environ['OPENAI_API_KEY']
# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {
#       "role": "user",
#       "content": ""
#     }
#   ],
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
# print(response)