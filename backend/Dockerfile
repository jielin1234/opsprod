# Use an official Python runtime as a parent image
FROM python:3.12.1-bullseye

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt ./

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 5001

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5001"]