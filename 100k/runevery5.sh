#!/bin/sh
killall python
python -u analyze.py top-100k.csv 50 2>&1 | tee -a project.log &
