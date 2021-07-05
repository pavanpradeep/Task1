# pull official base image
FROM python:3.8-buster

# set work directory
RUN mkdir /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy source code
COPY . .

ENTRYPOINT ["python3", "task1.py"]