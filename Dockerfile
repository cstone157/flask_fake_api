FROM alpine:latest
RUN apt-get install pip
#RUN apk update
#RUN apk add py-pip
#RUN apk add --no-cache python3-dev 
#RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
#RUN pip --no-cache-dir install -r requirements.txt
RUN pip install Flask
CMD ["python3", "app.py"]