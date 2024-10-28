# Use an official Python runtime as the base image
FROM python:3.8-slim

# Copy the current directory (our Flask app) into the container at /flask
COPY ./site /web/site
COPY ./flask-app.py /web/flask-app.py
COPY ./requirements.txt /web/requirements.txt

# Set the working directory in the container to /flask
WORKDIR /web

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV=development

# Make port 5000 available for the app
EXPOSE 5000

# Run the command to start the Flask app
#CMD ["flask", "run", "--host=0.0.0.0"]
#CMD ["python", "app.py"]
#CMD ["flask", "--app", "run", "--host=0.0.0.0"]
#CMD ["flask", "--app", "server", "run"]
#CMD ["flask", "--app", "flask", "run"]
CMD ["gunicorn", "flask-app:app", "-b", "0.0.0.0:5000", "-w", "4"]