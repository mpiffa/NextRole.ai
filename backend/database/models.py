# backend/database/models.py
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    
    # We replace full_name with three atomic fields
    first_name = Column(String(100), nullable=False)
    last_name_1 = Column(String(100), nullable=False)
    # nullable=True allows this field to be empty (for people with only one last name)
    last_name_2 = Column(String(100), nullable=True)
    
    professional_summary = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))