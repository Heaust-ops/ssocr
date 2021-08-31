#!/bin/bash
[ -d "env" ] && rm -rf env
python -m venv env
source env/bin/activate
pip install -r requirements.txt