import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai
from .prompts import PROMPT_TEMPLATE

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_resume_data(text):
    prompt = PROMPT_TEMPLATE.format(text=text)
    
    google_key = os.getenv("GOOGLE_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    # Try Gemini first
    if google_key and not google_key.startswith("your_"):
        try:
            model = genai.GenerativeModel('gemini-flash-latest')
            response = model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            if response.text:
                return json.loads(response.text)
        except Exception as e:
            print(f"Gemini extraction error: {e}")

    if openai_key and not openai_key.startswith("your_") and not openai_key == "dummy_key":
        try:
            client = OpenAI(api_key=openai_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                response_format={"type": "json_object"}
            )
            content = response.choices[0].message.content
            return json.loads(content)
        except Exception as e:
            print(f"OpenAI extraction error: {e}")
            raise e
    
    raise ValueError("No valid LLM API keys found or all providers failed.")
