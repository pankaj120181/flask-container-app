FROM ubuntu:16.04

ADD ./* /flaskcontainerapp

WORKDIR /flaskcontainerapp

RUN apt-get update -y && \ 
    apt-get install -y python3-pip python-dev

RUN pip3 install -r requirements.txt

ENV FLASK_ENV=development


ENTRYPOINT [ "python3" ]

CMD [ "server.py", "-h", "0.0.0.0", "-p", "5000" ]

