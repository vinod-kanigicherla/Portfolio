#!/bin/bash

tmux kill-server

cd /root/Portfolio

git fetch && git reset origin/main --hard

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

tmux new-session -d -s mysession "cd /root/Portfolio && source venv/bin/activate && flask run --host=0.0.0.0"
