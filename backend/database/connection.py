# backend/database/connection.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# We fetch the connection string securely from the environment variables
# If the variable is missing, it will raise an error early (Fail Fast principle)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is missing!")

# The engine is responsible for establishing the actual physical connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal will be used to create individual, temporary database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all our future database models
Base = declarative_base()

# Dependency to safely manage the database session lifecycle
def get_db():
    db = SessionLocal()
    try:
        # 'yield' pauses the function and hands the session to the API endpoint
        yield db
    finally:
        # This guarantees the session will always be closed, even if an error occurs
        db.close()
