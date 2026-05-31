# backend/main.py
# backend/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

# Import the database components
from database.connection import get_db, engine, Base
# IMPORTANT: We must import the models so SQLAlchemy knows they exist before creating the tables
from database import models, schemas

# 1. Initialize the database tables
# This command tells SQLAlchemy to create all tables defined in models.py
models.Base.metadata.create_all(bind=engine)

# 2. Initialize the application
app = FastAPI(title="NextRole.ai API")

@app.get("/")
def read_root():
    return {"message": "The FastAPI server for NextRole.ai is alive and running!"}

@app.get("/test-db")
def test_database_connection(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).scalar()
        return {
            "message": "Database connection successful!", 
            "result": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Database connection failed: {str(e)}"
        )
    
@app.post("/users", response_model=schemas.UserResponse, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Creates a new user profile in the database.
    """
    # Verification: Check if the email is already registered
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Mapping: Convert Pydantic schema to SQLAlchemy model
    new_user = models.User(
        email=user.email,
        first_name=user.first_name,
        last_name_1=user.last_name_1,
        last_name_2=user.last_name_2,
        professional_summary=user.professional_summary
    )
    
    # Transaction: Save to database
    db.add(new_user)       # Adds the object to the session
    db.commit()            # Commits the transaction to PostgreSQL
    db.refresh(new_user)   # Refreshes the object to get the generated ID and created_at
    
    # Response: FastAPI will automatically use response_model to format new_user
    return new_user