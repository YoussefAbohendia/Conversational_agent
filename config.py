import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

API_KEY=os.getenv("API_KEY")
WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")
BASE_URL=os.getenv("BASE_URL")
LLM_MODEL=os.getenv("LLM_MODEL")

print(f"API_KEY: {API_KEY}")
print(f"WEATHER_API_KEY: {WEATHER_API_KEY}")
print(f"BASE_URL: {BASE_URL}")
print(f"LLM_MODEL: {LLM_MODEL}")
