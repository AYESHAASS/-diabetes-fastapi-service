# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first (this speeds up builds)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the folders into the container
COPY ./app ./app
COPY ./model_bin ./model_bin

# Expose port 8000
EXPOSE 8000

# Command to run the API
<<<<<<< HEAD
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
=======
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
>>>>>>> 7408aa1597e107e5381463d0761bcdaeb2c7af9e
