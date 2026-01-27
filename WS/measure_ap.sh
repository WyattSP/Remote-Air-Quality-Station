#!/bin/bash
set -e

# Set directory
cd /home/pi/Documents/WS

# Run python script to log values
#python3 ap_bme680.py -i 300 -t 50400
python3 ap_bme680.py -i 5 -t 25

# Turn off pi
sudo shutdown -h now
