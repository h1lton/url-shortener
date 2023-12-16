from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MYSQL_ROOT_PASSWORD: str
    MYSQL_DATABASE: str

    DB_DSN: str
    DB_DSN_APP: str
    DB_DSN_TEST: str
    DB_NAME: str
    DB_TEST_NAME: str

    DB_ECHO: bool = False

    STANDARD_LENGTH_PATH: int = 8
    MIN_LENGTH_PATH: int = 3
    MAX_LENGTH_PATH: int = 64

    LIST_OF_DENIED_PATHS: list[str] = ["docs"]

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
