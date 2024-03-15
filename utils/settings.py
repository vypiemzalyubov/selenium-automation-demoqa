from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv('.env.example'))


class UISettings(BaseSettings):
    BASE_PAGE: str

    @property
    def base_page(self):
        return self.BASE_PAGE

    class ConfigDict:
        env_file = '.env.example'
        env_file_encoding = 'utf-8'


settings = UISettings()
