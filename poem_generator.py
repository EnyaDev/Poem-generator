from google import genai
import os
from dotenv import load_dotenv


#Loading hidden variables
load_dotenv()

#Getting API Key securely
MY_API_KEY = os.getenv("GEMINI_API_KEY")


#1. We start with the client talk with Gemini

client = genai.Client(api_key=MY_API_KEY)

#2. Define what we want Gemini to write
prompt = (
    "Write a short poem or haiku about a broken heart."
    "Focus on themes of meeting someone for the first time, love at  first sight"
    "and feeling head over heels about someone you might not even talk to"
)

print("Thinking about a poem...\n")

#3. Sending prompt to Gemini
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)

#4. Print poetry
print("Here is your poem:\n")
print(response.text)