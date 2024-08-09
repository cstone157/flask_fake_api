FROM alpine:3.19

RUN apt-get install pip

WORKDIR /app
COPY ./app /app

RUN pip install Flask 
CMD ["python3", "app.py"]