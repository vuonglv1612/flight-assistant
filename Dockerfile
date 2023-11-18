FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app

# Install some packages needed for building the python packages
RUN apt update && apt install build-essential libpq-dev -y && rm -rf /var/libs/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app
