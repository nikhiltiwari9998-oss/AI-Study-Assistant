import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_pdf_question(pdf_text, question):

    prompt = f"""
You are an AI Study Assistant.

Study the following PDF content carefully and answer ONLY from the given content.

PDF Content:
{pdf_text}

Question:
{question}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {e}"