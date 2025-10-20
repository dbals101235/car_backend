import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

# .env 파일 읽기
load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
if not MONGODB_URL:
    raise ValueError("MONGODB_URL 환경변수 설정이 필요합니다!")

# MongoDB 연결
client = AsyncIOMotorClient(MONGODB_URL)
db = client.get_database()  # mydatabase 자동 선택

async def test_connection():
    try:
        # 테스트용 컬렉션 조회
        collections = await db.list_collection_names()
        print("MongoDB 연결 성공! 컬렉션 목록:", collections)
    except Exception as e:
        print("MongoDB 연결 실패:", e)

asyncio.run(test_connection())
