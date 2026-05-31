# backend/database/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

# Schema for INPUT data (what the user sends to us)
class UserCreate(BaseModel):
    # EmailStr automatically validates that the string has a valid email format (@)
    email: EmailStr
    first_name: str
    last_name_1: str
    last_name_2: Optional[str] = None
    professional_summary: Optional[str] = None

# Schema for OUTPUT data (what we send back to the user)
class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    first_name: str
    last_name_1: str
    last_name_2: Optional[str] = None
    professional_summary: Optional[str] = None
    created_at: datetime

    class Config:
        # This tells Pydantic to read data even if it's not a standard Python dictionary
        # (It allows reading directly from SQLAlchemy models)
        from_attributes = True