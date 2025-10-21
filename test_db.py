import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from config import config

async def test_mongo():
    # MongoDB 클라이언트 생성
    client = AsyncIOMotorClient(config.DB_URL)
    db = client[config.DB_NAME]

    # 컬렉션 이름 확인
    collections = await db.list_collection_names()
    print(f"Connected to DB: {config.DB_NAME}")
    print("Collections:", collections)

    # 테스트용 문서 삽입
    test_doc = {"name": "Test Car", "brand": "Hyundai", "year": 2023}
    result = await db.test_collection.insert_one(test_doc)
    print("Inserted document ID:", result.inserted_id)

    # 테스트용 문서 삭제
    await db.test_collection.delete_one({"_id": result.inserted_id})
    print("Test document deleted")

    # 연결 종료
    client.close()

# asyncio 실행
if __name__ == "__main__":
    asyncio.run(test_mongo())
