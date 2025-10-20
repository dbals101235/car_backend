from typing import Optional, Annotated, List
from pydantic import BaseModel, ConfigDict, Field, BeforeValidator, field_validator

# ObjectId처럼 처리할 타입 정의
PyObjectId = Annotated[str, BeforeValidator(str)]

# -------------------------------
# 차량 모델
# -------------------------------
class CarModel(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")  # 기본값 None으로 수정
    brand: str = Field(...)
    make: str = Field(...)
    year: int = Field(..., gt=1970, lt=2025)
    cm3: int = Field(..., gt=0, lt=5000)
    km: int = Field(..., gt=0, lt=500000)
    price: int = Field(..., gt=0, lt=100000)

    # 브랜드 첫 글자 대문자
    @field_validator("brand")
    @classmethod
    def check_brand_case(cls, v: str) -> str:
        return v.title()

    # 모델 첫 글자 대문자
    @field_validator("make")
    @classmethod
    def check_make_case(cls, v: str) -> str:
        return v.title()

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "brand": "Ford",
                "make": "Fiesta",
                "year": 2019,
                "cm3": 1500,
                "km": 120000,
                "price": 10000,
            }
        },
    )

# -------------------------------
# 수정용 모델
# -------------------------------
class UpdateCarModel(BaseModel):
    brand: Optional[str] = Field(None)
    make: Optional[str] = Field(None)
    year: Optional[int] = Field(None, gt=1970, lt=2025)
    cm3: Optional[int] = Field(None, gt=0, lt=5000)
    km: Optional[int] = Field(None, gt=0, lt=500000)
    price: Optional[int] = Field(None, gt=0, lt=100000)

# -------------------------------
# 컬렉션 모델
# -------------------------------
class CarCollection(BaseModel):
    cars: List[CarModel]

# -------------------------------
# 테스트용 코드
# -------------------------------
if __name__ == "__main__":
    test_car_1 = CarModel(
        brand="ford",
        make="fiesta",
        year=2019,
        cm3=1500,
        km=120000,
        price=10000
    )
    test_car_2 = CarModel(
        brand="fiat",
        make="stilo",
        year=2003,
        cm3=1600,
        km=320000,
        price=3000
    )
    car_list = CarCollection(cars=[test_car_1, test_car_2])
    print(car_list.model_dump())
