#!/bin/bash
[ ! -d "env" ] && sh ./build.sh
source env/bin/activate
python main.py