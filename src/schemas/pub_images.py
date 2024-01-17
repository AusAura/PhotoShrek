from typing import Optional

from pydantic import BaseModel, Field, field_validator


class BaseImageSchema(BaseModel):
    pass


class CurrentImageSchema(BaseImageSchema):
    current_img: Optional[str] = None


class UpdatedImageSchema(BaseImageSchema):
    updated_img: Optional[str] = None


class QrCodeImageSchema(BaseImageSchema):
    qr_code_img: Optional[str] = None


class PubImageSchema(CurrentImageSchema, UpdatedImageSchema, QrCodeImageSchema):
    pass


class TransformationKey(BaseModel):
    key: str = Field()

    @field_validator("key")
    def validate_key(cls, key: str) -> str:   # noqa
        if key not in ["left", "right", "filter"]:
            raise ValueError(f"Invalid transformation key: {key}")
        return key