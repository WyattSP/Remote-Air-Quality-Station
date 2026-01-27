sudo raspi-config nonint do_wifi_ssid_passphrase name password

hostname -I

# To move file from mac -> pi 
scp /Users/wyatt.petryshen/Documents/GitHub/Remote-Air-Quality-Station/c_temp/apartment_conditions.py pi@192.168.0.24:/home/pi/Documents/AQ/Remote-Air-Quality-Station-main/libs

scp /Users/wyatt.petryshen/Documents/GitHub/Remote-Air-Quality-Station/WS/ap_bme680.py pi@raspberrypi.local:/home/pi/Documents/WS

# SSH onto pi
ssh pi@192.168.0.24
#or
ssh pi@raspberrypi.local
# then enter password

# cd into directory
cd Documents/AQ/Remote-Air-Quality-Station-main/libs

# run 
python3 apartment_conditions.py

# Get data off pi
scp pi@192.168.0.24:/home/pi/Desktop/apartment_log.txt ~/Desktop/

# Turn pi off 
sudo shutdown -h -P now


# Get data off pi
scp pi@raspberrypi.local:/home/pi/Desktop/apartment_log.txt ~/Documents/GitHub/Remote-Air-Quality-Station/WS/OutPut