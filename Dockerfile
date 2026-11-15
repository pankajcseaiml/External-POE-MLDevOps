# Step 9: Lightweight Python base image
FROM python:3.11-slim

# Set container working directory
WORKDIR /app

# Install project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 10: Copy multiplication application code
COPY main.py hello.py ./

# Expose FastAPI web service port
EXPOSE 8000

# Default execution: run multiplication program
CMD ["python", "hello.py"]
