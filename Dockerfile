FROM python:3.6-alpine3.7 as builder
MAINTAINER mrmoneyc <moneyc.net@gmail.com>

RUN apk add --no-cache build-base mariadb-dev
WORKDIR /opt
ADD backend/requirements.txt /opt
RUN pip install virtualenv
RUN virtualenv pyvenv
RUN /bin/sh -c "source /opt/pyvenv/bin/activate && pip install -r requirements.txt && deactivate"

FROM python:3.6-alpine3.7
COPY --from=builder /opt/pyvenv /opt/pyvenv

ADD backend /opt/flask-todo
ADD entry.sh /bin
WORKDIR /opt/flask-todo

ENTRYPOINT ["/bin/entry.sh"]
