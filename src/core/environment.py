import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv("OPEN_API_KEY")
MODEL = 'gpt-4o-mini'
openai = OpenAI()
