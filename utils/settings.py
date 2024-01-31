from pydantic_settings import BaseSettings
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env.example"))


class Settings(BaseSettings):
    BASE_PAGE: str

    @property
    def base_page(self):
        return self.BASE_PAGE

    class ConfigDict:
        env_file = ".env.example"


settings = Settings()
