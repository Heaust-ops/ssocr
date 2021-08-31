#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd $SCRIPT_DIR
[ -d "env" ] && rm -rf env
python -m venv env
source env/bin/activate
pip install -r requirements.txt