from app.providers.gemini import GeminiProvider
from app.providers.openrouter import OpenRouterProvider


class AIRouter:

    def __init__(self):
        self.providers = {
            "gemini": GeminiProvider(),
            "openrouter": OpenRouterProvider(),
        }

    async def chat(self, prompt: str, provider: str = "gemini") -> str:

        if provider not in self.providers:
            raise ValueError(f"Unknown provider: {provider}")

        return await self.providers[provider].chat(prompt)
