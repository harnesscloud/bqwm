FROM python:2.7
MAINTAINER Mark Stillwell <mark@stillwell.me>

ADD . /service
WORKDIR /service
RUN pip install -r requirements.txt

CMD python runserver.py
EXPOSE 5000
