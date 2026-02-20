import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    # ScaleDown API key
    SCALEDOWN_API_KEY: str = os.getenv("SCALEDOWN_API_KEY")

    # Google API keys (if needed later)
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET")

    # Maps API key (for travel time calculation)
    MAPS_API_KEY: str = os.getenv("MAPS_API_KEY")

    # Other environment configs
    ENV: str = os.getenv("ENV", "development")

# Create a global settings instance
settings = Settings()