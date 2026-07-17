from abc import ABC, abstractmethod


class BaseProvider(ABC):
    name = "Base"

    @abstractmethod
    async def chat(self, prompt: str) -> str:
        """
        Send a prompt to the provider.
        Returns the model response.
        """
        pass

    async def health_check(self) -> bool:
        return True