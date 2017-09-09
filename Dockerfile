FROM ubuntu:17.10

# update apt and install git and python3
RUN apt-get update -y
RUN apt-get install -y git python3

# ssh stuff
# RUN mkdir -p /root/.ssh/
# ADD repo_key /root/.ssh/id_rsa
# RUN echo "    IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config
# RUN chmod 600 /root/.ssh/id_rsa
# RUN touch /root/.ssh/known_hosts
# RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

# get fuckoffbot aboard
RUN mkdir -p /fuckoffbot
RUN git clone git@github.com:SupBrah/slackbot.git fuckoffbot/
WORKDIR /fuckoffbot

# run it
# RUN run.py
