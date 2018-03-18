FROM python:3.6
MAINTAINER mrmoneyc <moneyc.net@gmail.com>

ADD src /opt/flask-todo
WORKDIR /opt/flask-todo
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/opt/flask-todo/app.py"]
