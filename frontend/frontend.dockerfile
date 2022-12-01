FROM python:3.9-slim-buster

WORKDIR /code_front

RUN apt-get update && apt-get install -y procps && pip install -U pip \
    && rm /etc/localtime  \
    && ln -s /usr/share/zoneinfo/America/Mexico_City /etc/localtime

COPY ./requirements.txt /code_front/requirements.txt

RUN pip install -r ./requirements.txt

COPY cnn-app.py /code_front/cnn-app.py

EXPOSE 8501

CMD ["streamlit", "run", "cnn-app.py", "--server.port=8501", "--server.address=0.0.0.0"]