# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory (our Flask app) into the container at /app
COPY ./app /app

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=flask-api.py
ENV FLASK_ENV=development

# Make port 8000 available for the app
EXPOSE 8000
EXPOSE 5000

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
#CMD ["python", "app.py"]
