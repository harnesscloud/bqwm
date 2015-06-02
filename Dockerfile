FROM phusion/baseimage:latest
MAINTAINER Mark Stillwell <mark@stillwell.me>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y install \
        curl \
        python && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN curl -s https://bootstrap.pypa.io/get-pip.py | python -

WORKDIR /service
ADD requirements.txt /service/
RUN pip install -r requirements.txt
ADD . /service

RUN ln -s runapp.py /etc/my_init.d/10-runapp.py

EXPOSE 80
