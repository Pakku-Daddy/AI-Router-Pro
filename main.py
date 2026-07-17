import asyncio

from app.router.router import AIRouter


async def main():

    router = AIRouter()

    provider = input(
        "Choose provider (gemini/openrouter): "
    ).strip().lower()

    prompt = input("You: ")

    answer = await router.chat(
        prompt=prompt,
        provider=provider,
    )

    print("\nAssistant:\n")
    print(answer)


if __name__ == "__main__":
    asyncio.run(main())