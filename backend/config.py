# .env -> API Keys -> Constants


"""
Application configuration.

Loads environment variables and exposes them
to the rest of the application.

USAGE : 
from backend.config import settings

print(settings.MODEL_NAME)

"""

from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    # -----------------------------
    # API Keys
    # -----------------------------

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    # -----------------------------
    # LLM
    # -----------------------------

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "gemini-2.5-flash"
    )

    TEMPERATURE = float(
        os.getenv(
            "TEMPERATURE",
            "0.3"
        )
    )

    # -----------------------------
    # Workflow
    # -----------------------------

    MAX_RETRIES = int(
        os.getenv(
            "MAX_RETRIES",
            "2"
        )
    )


settings = Settings()