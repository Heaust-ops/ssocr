#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
[ ! -d "$SCRIPT_DIR/env" ] && sh $SCRIPT_DIR/build.sh
source $SCRIPT_DIR/env/bin/activate
python $SCRIPT_DIR/main.py