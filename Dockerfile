# set base image (host OS)
FROM python:3

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .
ARG DEBIAN_FRONTEND=noninteractive

# install dependencies
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install ffmpeg
RUN pip install -r requirements.txt


# copy the content of the local src directory to the working directory
COPY src/ .



CMD python ./main.py