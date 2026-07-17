import asyncio

from app.providers.gemini import GeminiProvider


async def main():
    ai = GeminiProvider()

    answer = await ai.chat("Say hello in one sentence.")

    print("\nGemini replied:\n")
    print(answer)


if __name__ == "__main__":
    asyncio.run(main())