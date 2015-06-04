FROM python:2.7
MAINTAINER Mark Stillwell <mark@stillwell.me>

ADD . /srv/bqwm
WORKDIR /srv/bqwm
RUN pip install -U -r requirements.txt
RUN pip install -U -e .

CMD bqwmd --nofork
EXPOSE 5000
