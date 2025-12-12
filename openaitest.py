import os
import google.generativeai as genai
from config import gemini_key 

genai.configure(api_key=gemini_key)

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Write an email to my boss for resignation?")

print(response.text)