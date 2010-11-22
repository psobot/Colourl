#!/bin/sh
killall python
python -u ./100k/analyze.py ./100k/top-100k.csv 50 2>&1 | tee -a ./100k/project.log &
