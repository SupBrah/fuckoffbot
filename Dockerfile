FROM ubuntu:17.10

# update apt and install git and python3
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip

# ssh stuff
RUN mkdir -p /root/.ssh/

# get fuckoffbot aboard
RUN mkdir -p /fuckoffbot
COPY . /fuckoffbot/

# change to our workdir
WORKDIR /fuckoffbot

# install pip modules
RUN pip3 install -r requirements.txt

# run it
RUN run.py
