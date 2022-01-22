FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev
WORKDIR /app
ADD requirements.txt /app/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/
