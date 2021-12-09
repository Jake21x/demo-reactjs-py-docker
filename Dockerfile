FROM python:3.7-alpine

WORKDIR /home/ 
COPY ./requirements.txt .

RUN apk update \
    && apk add --virtual build-deps gcc libffi-dev openssl-dev libxml2-dev jpeg-dev zlib-dev openjpeg-dev python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apk del build-deps
  
COPY . .

RUN mkdir -p app/static/uploads
RUN mkdir -p app/static/video
RUN mkdir -p app/static/uploads/file 
RUN mkdir -p app/static/uploads/media 
RUN mkdir -p app/static/uploads/photo
RUN mkdir -p app/static/uploads/signature
RUN mkdir -p app/static/uploads/template
RUN mkdir -p logs


CMD "python3" "application.py"