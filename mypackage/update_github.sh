#!/bin/bash

cd /home/pi/PythonProjects/epg
python ./mypackage/test.py  >>/home/pi/PythonProjects/epg/mypackage/log.txt 2>&1
cd /home/pi/PythonProjects/river2718.github.io
git pull >>/home/pi/PythonProjects/epg/mypackage/log.txt 2>&1
git add . >>/home/pi/PythonProjects/epg/mypackage/log.txt 2>&1
git commit -m 'Update urls' >>/home/pi/PythonProjects/epg/mypackage/log.txt 2>&1
git push >>/home/pi/PythonProjects/epg/mypackage/log.txt 2>&1
