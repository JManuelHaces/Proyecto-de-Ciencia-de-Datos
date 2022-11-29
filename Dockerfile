FROM python:3.9-slim-buster

WORKDIR /code

RUN apt-get update && apt-get install -y procps && pip install -U pip \
    && rm /etc/localtime  \
    && ln -s /usr/share/zoneinfo/America/Mexico_City /etc/localtime

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r ./requirements.txt

COPY ./CNN_Resnet.pkl  /CNN_Resnet.pkl

COPY ./main.py /code/main.py

COPY ./frontend/cnn-app.py /code/frontend/cnn-app.py

COPY ./start.sh ./start.sh

EXPOSE 8501

EXPOSE 8001

CMD ["bash", "./start.sh"]