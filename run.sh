#!/bin/sh
killall python
echo "Python killed."
cd /var/www/colour.petersobot.com/100k/
python -u analyze.py top-100k.csv 50 2>&1 | tee -a project.log &
echo "Python process restarted."

