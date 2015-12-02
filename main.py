#!/usr/bin/env python3
from gps_python import *

if __name__ == "__main__":

    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    try:
        while True:

            report = session.next()
            print(report)

            if report['class'] == 'DEVICE':
                session.close()
                session = gps(mode=WATCH_ENABLE)

    except StopIteration:
        print("GPSD has terminated")
