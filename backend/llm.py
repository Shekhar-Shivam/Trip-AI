# call_llm(prompt)

"""
USAGE :

from backend.llm import llm_service

answer = llm_service.invoke(
    "Tell me about Goa."
)

print(answer)
"""

"""
LLM wrapper.

If tomorrow you replace Gemini with OpenAI,
only this file changes.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from backend.config import settings


class LLMService:

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(

            model=settings.MODEL_NAME,
            google_api_key=settings.GEMINI_API_KEY,
            temperature=settings.TEMPERATURE,
            convert_system_message_to_human=True
        )

    def invoke(self, prompt: str):
        """
        Simple synchronous call.
        """
        response = self.llm.invoke(prompt)
        return response.content


llm_service = LLMService()
