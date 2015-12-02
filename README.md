# GPSLogger

Simple GPS Logger for Raspberry PI

## Hardware
Tested on :
* Raspberry PI 2
* Adafruit Ultimate GPS Breakout : <http://www.adafruit.com/product/746>

## Software
* Python 3.4
* GPSD

## Setup

### Install GPSD

```sh
sudo apt-get install gpsd gpsd-clients libgps-dev
```

### Connecting the GPS
Here is a good How To :
<https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi/>

#### Step 1
```sh
sudo nano /boot/cmdline.txt
```
Change :
```sh
dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
```
To :
```sh
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
```

#### Step 2
```sh
sudo nano /etc/default/gpsd
```
And change the next two following lines :
```sh
DEVICES="/dev/ttyUSB0"

GPSD_OPTIONS="-n"
```

#### Step 3
Reboot

#### Step 4
Check if GPSD is working properly
```sh
cgps -s
```

## Start
```sh
./main.py
```
