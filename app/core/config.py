from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    MAIL: str = ''
    MAIL_PASSWORD: str = ''

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

settings = AppSettings()