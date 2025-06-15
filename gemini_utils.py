import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_story_from_caption(caption: str) -> str:
    prompt = (
        f"Write a vivid short story about this scene: '{caption}'. "
        "Add emotion, imagination, and a sense of place."
    )
    response = model.generate_content(prompt)
    return response.text.strip()
