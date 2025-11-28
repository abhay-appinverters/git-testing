# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict
# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "My First FastAPI App"
    env: str = "dev"
    api_v2_prefix: str = "/api_v2"
    debug: bool = True
    api_prefix: str

    # future fields:
    # openai_api_key: str | None = None
    # dynamodb_table_name: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # ignore unknown env vars
    )

settings = Settings()
