from fastapi import APIRouter, status, UploadFile, File, Form
from typing import Optional
from models import CarModel
from database import db
import cloudinary
import cloudinary.uploader

# ✅ Cloudinary 설정
cloudinary.config(
    cloud_name="drnbc16jt",
    api_key="184846872663594",
    api_secret="956YwWtFpL13iM4704KN3ov5uek",
    secure=True
)

router = APIRouter()

# ✅ 차량 목록 조회 (GET)
@router.get("/", response_model=list[CarModel])
async def get_cars():
    cars = []
    async for car in db.cars.find():
        car["_id"] = str(car["_id"])  # ObjectId를 문자열로 변환
        del car["_id"]
        cars.append(car)
    return cars


# ✅ 차량 등록 (POST)
@router.post("/", response_model=CarModel, status_code=status.HTTP_201_CREATED)
async def create_car(
    brand: str = Form(...),
    make: str = Form(...),
    year: int = Form(...),
    cm3: int = Form(...),
    km: int = Form(...),
    price: int = Form(...),
    picture: Optional[UploadFile] = File(None)
):
    car_dict = {
        "brand": brand,
        "make": make,
        "year": year,
        "cm3": cm3,
        "km": km,
        "price": price,
    }

    # ✅ 사진이 있으면 Cloudinary에 업로드
    if picture:
        upload_result = cloudinary.uploader.upload(
            picture.file,
            folder="car_images"
        )
        car_dict["image_url"] = upload_result.get("secure_url")

    # ✅ MongoDB에 저장
    result = await db.cars.insert_one(car_dict)
    created_car = await db.cars.find_one({"_id": result.inserted_id})
    created_car["_id"] = str(created_car["_id"])

    return CarModel(**created_car)

