#!/bin/bash

# rsync -ahv /home/pi/work/mp4 rsh:/home/is/takumi-fu/2022_camera_data
rsync -ahvu /home/pi/work/mp4 rsh:/project/inet-its/2022-image-busstop
find /home/pi/work/mp4/ -mtime +7 -exec rm {} \;
