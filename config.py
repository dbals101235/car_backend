from pydantic_settings import BaseSettings

class BaseConfig(BaseSettings):
    # MongoDB
    DB_URL: str = "mongodb+srv://dldbals101235_db_user:FBUaT48IopuSka8f@yumin.9c7uuiu.mongodb.net/"
    DB_NAME: str = "carBackend"

    # Cloudinary
    CLOUDINARY_CLOUD_NAME: str = "drnbc16jt"
    CLOUDINARY_API_KEY: str = "184846872663594"
    CLOUDINARY_API_SECRET: str = "956YwWtFpL13iM4704KN3ov5uek"

config = BaseConfig()  # 인스턴스는 한 번만 생성
