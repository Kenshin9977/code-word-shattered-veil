# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose Fly.io's required port
EXPOSE 8080

# Start the app
CMD ["python", "main.py"]