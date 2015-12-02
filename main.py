#!/usr/bin/env python3
from gps import *

if __name__ == "__main__":

    session = gps(mode=WATCH_ENABLE)
    try:
        while True:

            report = session.next()
            print(report)

            if report['class'] == 'DEVICE':
                session.close()
                session = gps(mode=WATCH_ENABLE)

    except StopIteration:
        print("GPSD has terminated")
