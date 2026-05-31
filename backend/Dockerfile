# backend/Dockerfile

# Base image for python
FROM python:3.14-slim

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Start uvicorn (development)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]