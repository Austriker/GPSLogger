#!/usr/bin/env python3
from gps3 import gps3
import time

if __name__ == "__main__":

    connection = gps3.GPSDSocket()
    fix = gps3.Fix()

    try:
        for data in connection:
            if data:
                fix.refresh(data)
            else:
                pass

            time.sleep(1)

    except KeyboardInterrupt:
        connection.close()
        print("\nTerminated by user\nGood Bye.\n")
