from fastapi import FastAPI
from routers import cars  # cars.py 라우터 불러오기

app = FastAPI()

# ✅ 차량 라우터 등록
app.include_router(cars.router, prefix="/cars", tags=["Cars"])

# 기본 경로 테스트용
@app.get("/")
def root():
    return {"message": "Server is running 🚀"}
