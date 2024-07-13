#!/bin/bash

cd /root/Portfolio

git fetch && git reset origin/main --hard

source /root/Portfolio/python3-virtualenv/bin/activate

pip3 install -r requirements.txt

sudo systemctl restart myportfolio
