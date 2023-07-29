from pydantic import BaseSettings

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    WEATHER_TOKEN: str

    class Config:
        env_file = ".env"


settings = Settings()