from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_URL: str

    @property
    def base_url(self):
        return f"{self.BASE_URL}"

    class ConfigDict:
        env_file = ".env"


settings = Settings()
