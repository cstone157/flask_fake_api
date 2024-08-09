#FROM alpine:3.19
#
#RUN apt-get install pip
#
#WORKDIR /app
#COPY ./app /app
#
#RUN pip install Flask 
#CMD ["python3", "app.py"]


# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory (our Flask app) into the container at /app
COPY ./app /app

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN export FLASK_APP=flask-api.py
RUN export FLASK_ENV=development

# Make port 5000 available for the app
EXPOSE 5000

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
