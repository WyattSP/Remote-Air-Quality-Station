# Remote Air Quality Station
 Remote PM 2.5 SDS011 air quality station with temperature and humidity.


## dependencies

pip install python-aqi

## Commands from terminal

- Connect to pi using ssh in shell
- Check working directory
```bash
pi@raspberry:~ $ pwd
```
Change directory to desired file save location
```bash
pi@raspberry:~ $ cd /home/pi/directory
```
Run test script and check output
```bash
pi@raspberry:~/home/pi/directory $ python3 test.py
```
Run Sensor. Output will stream in the shell until run is complete.
```bash
pi@raspberry:~/home/pi/directory $ python3 senseAir.py -a 1 -r 10 -n 001
```
Transfer log file from pi onto local computer
```bash
pi@raspberry:~/home/pi/directory $ get /log_files/aq_log_001.txt

#or

$ scp -rv aq_log_001.txt pi@IP:/path/to/copy/of/aq_log_001/
```
