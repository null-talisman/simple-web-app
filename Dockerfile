# use ubuntu 20.04 as base image
FROM ubuntu:20.04
# run apt-get update, apt-get upgrade and apt-get autoremove
RUN apt-get update && apt-get install apt-utils -y && apt-get upgrade -y \
  && apt-get autoremove -y
# install python3 & pip
RUN apt-get install python3 python3-pip -y
RUN python3 -m pip install --upgrade pip
# copy files to app dir
RUN mkdir app/
WORKDIR /app
ADD my_app/ .
# install requirements
RUN python3 -m pip install -r requirements.txt
# run program
CMD python3 my_app.py
