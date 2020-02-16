#! /bin/bash

export PYTHONPATH=../src/

python3 -m unittest discover . -p "*_tests.py"
