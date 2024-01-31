from pydantic_settings import BaseSettings
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env.example"))


class UISettings(BaseSettings):
    base_page: str

    @property
    def base_page(self):
        return self.base_page

    class ConfigDict:
        env_file = ".env.example"
        env_file_encoding = "utf-8"


settings = UISettings()
