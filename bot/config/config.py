from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: 28354723
    API_HASH: 41e7ce41a7b75cc2a109133bb4d73156
   
    REF_ID: str = '7240829185'
    SUBSCRIBE_HIDDEN_CODE: bool = True
    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [0, 15]
    FAKE_USERAGENT: bool = True
    SLEEP_TIME: list[int] = [1800, 3600]
    
    USE_PROXY_FROM_FILE: bool = False


settings = Settings()


