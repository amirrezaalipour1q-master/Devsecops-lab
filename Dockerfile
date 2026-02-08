# Base Image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file FIRST
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Command to run the application
CMD ["python", "app.py"]
