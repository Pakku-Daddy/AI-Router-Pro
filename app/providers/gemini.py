from google import genai

from app.config import settings
from app.providers.base import BaseProvider


class GeminiProvider(BaseProvider):
    name = "Gemini"

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

    async def chat(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        return response.text