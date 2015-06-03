FROM phusion/baseimage:latest
MAINTAINER Mark Stillwell <mark@stillwell.me>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y install \
        curl \
        python && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN curl -s https://bootstrap.pypa.io/get-pip.py | python -

ADD . /service
WORKDIR /service
RUN pip install -r requirements.txt
RUN pip install -e .

RUN ln -s runserver.py /etc/my_init.d/10-runserver.py

EXPOSE 5000
