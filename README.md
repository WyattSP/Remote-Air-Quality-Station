# Remote Air Quality Station

**Work in Progress**

 Remote PM 2.5 SDS011 air quality station with temperature and humidity.


## Dependencies

pip install python-aqi
pip install plotly

## Commands from terminal
Workflow:

Prior to remotely running headless pi, connect local laptop and pi to a wireless hotspot and record the pi's IP address.

When powering on the pi, make sure wireless hotspot is connected to both devices.

Tip: If pi cannot connect, open Personal Hotspot in Settings on your iphone and leave it open. Running ssh bash command to connect to the pi should then work.

Connect to pi using ssh in shell
```bash
ssh pi@IP
```
Check working directory
```bash
pi@raspberry:~ $ pwd
```
Change directory to desired file save location
```bash
pi@raspberry:~ $ cd /home/pi/directory
```
To check list of files in directory use:
```bash
ls
```
Run test script and check output
```bash
pi@raspberry:~/home/pi/directory $ python3 test.py
```
Run Sensor. Output will stream in the shell until run is complete.
```bash
pi@raspberry:~/home/pi/directory $ python3 senseAir.py -a 1 -r 100
```
Transfer log file from pi onto local computer. Remember to change your directory on your local machine to the location where you want the file saved. Run this from local bash in new shell terminal. Make sure not to disconnect ssh connection with pi (this might actually not matter).
```bash
scp pi@IP:/home/pi/directory/aq_log.txt aq_log.txt
```
To turn off the pi from the shell
```bash
sudo shutdown -h -P now
```
After file is saved. Open terminal and run plot_ssd.py script. Make sure file is located in your current working directory. At the moment, the path to the air quality log file is not set. Open plot_ssd.py in a text editor and edit line 15 to the path of your now saved log file.

```python
path = r'Path' #edit this line such that the log file can be found
```
After plot_ssd.py has been edited and saved run in terminal:
```base
python plot_ssd.py
```
A plot of the air quality data should appear in your safari browser. If it does not, you may need to install plotly first onto your machine using pip.
