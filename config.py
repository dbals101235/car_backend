from pydantic_settings import BaseSettings

class BaseConfig(BaseSettings):
    # MongoDB
    DB_URL: str
    DB_NAME: str

    # Cloudinary
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str

    class Config:
        env_file = ".env"  # .env 파일에서 설정 읽기

# 인스턴스는 한 번만 생성
config = BaseConfig()