# Use an official Python runtime as a parent image
FROM python:3.8-slim
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install Flask
RUN pip install --no-cache-dir flask

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3-dev libpq-dev

# Install psycopg2
RUN pip install psycopg2

# Run app.py when the container launches
CMD ["python", "src/app.py"]
