# Use the official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port Flet uses
EXPOSE 8080

# Start the Flet app
