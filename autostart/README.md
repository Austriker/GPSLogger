# Setup

To start the logger at startup under Debian 8

## Adding a service to Systemd

First copy the config file :
```sh
sudo mkdir /usr/lib/systemd/system
sudo cp /home/pi/GPSLogger/autostart/gpslogger.service /usr/lib/systemd/system/gpslogger.service
```

Then refresh the systemd :
```sh
systemctl daemon-reload
```

Now you can start the service :
```sh
systemctl start gpslogger
```

You can check if it's working :
```sh
systemctl status gpslogger
```

Finaly you need to enable the service at startup :
```sh
systemctl enable gpslogger
```

