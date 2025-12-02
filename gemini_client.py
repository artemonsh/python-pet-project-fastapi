from google import genai

from config import config_obj

client = genai.Client(api_key=config_obj.gemini_api_key)


def get_answer_from_gemini(prompt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )
    return response.text
