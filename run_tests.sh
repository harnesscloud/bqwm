#!/bin/bash
apt-get update
apt-get install curl python
curl -s https://bootstrap.pypa.io/get-pip.py | python -
pip install -r requirements.txt
pip install -e .
python setup.py test
