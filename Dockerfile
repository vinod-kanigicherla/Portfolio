# Use the official Python 3.9 slim image
FROM python:3.9-slim-buster

# Set the working directory inside the container to /myportfolio
WORKDIR /myportfolio

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the default command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]

# Expose port 5000 to the host machine
EXPOSE 5000
