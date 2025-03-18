from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_input = input("Enter the text you want to generate content for: ")
response = client.models.generate_content_stream(  
    model="gemini-2.0-flash", 
    contents=user_input
)
for chunk in response:
    print(chunk.text, end="")