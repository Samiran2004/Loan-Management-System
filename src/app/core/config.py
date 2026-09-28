from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Customer Risk & Loan Platform"
    environment: str = "development"
    
    mongodb_url: str = ""
    mongodb_database: str = "risk_platform"
    
    imagekit_private_key: str | None = None
    imagekit_url_endpoint: str | None = None
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

settings = Settings()