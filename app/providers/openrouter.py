from openai import AsyncOpenAI

from app.config import settings
from app.providers.base import BaseProvider


class OpenRouterProvider(BaseProvider):
    name = "OpenRouter"

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )

        # Default model
        self.model = "openai/gpt-oss-20b"

    async def chat(self, prompt: str) -> str:

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content