# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7-slim-stretch

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /app
# Set the working directory to /music_service
WORKDIR /app
COPY . /app
ADD . /app

EXPOSE 8000

RUN ls
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

CMD python3 app.py runserver 0.0.0.0:5000