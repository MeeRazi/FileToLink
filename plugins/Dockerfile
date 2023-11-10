# Use a base image with Python installed
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy local files to the container
COPY . /app/

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose port 8080 for Flask
EXPOSE 8080

# Command to run the application
CMD ["python", "bot.py"]
