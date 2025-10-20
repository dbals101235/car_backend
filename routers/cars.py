from fastapi import APIRouter, status, UploadFile, File, Form
from typing import Optional
from models import CarModel
from database import db
import cloudinary
import cloudinary.uploader

# Cloudinary 설정
cloudinary.config(
    cloud_name="drnbc16jt",
    api_key="184846872663594",
    api_secret="956YwWtFpL13iM4704KN3ov5uek",
    secure=True
)

router = APIRouter()

@router.post("/", response_model=CarModel, status_code=status.HTTP_201_CREATED)
async def create_car(
    brand: str = Form(...),
    make: str = Form(...),
    year: int = Form(...),
    cm3: int = Form(...),
    km: int = Form(...),
    price: int = Form(...),
    picture: Optional[UploadFile] = File(None)  # 여기서 변수 이름 picture로
):
    car_dict = {
        "brand": brand,
        "make": make,
        "year": year,
        "cm3": cm3,
        "km": km,
        "price": price,
    }

    # 파일이 있으면 Cloudinary 업로드
    if picture:
        upload_result = cloudinary.uploader.upload(
            picture.file,  # picture.file로 업로드
            folder="car_images"
        )
        car_dict["image_url"] = upload_result.get("secure_url")

    # MongoDB에 저장
    result = await db.cars.insert_one(car_dict)
    created_car = await db.cars.find_one({"_id": result.inserted_id})
    created_car["_id"] = str(created_car["_id"])

    return CarModel(**created_car)
