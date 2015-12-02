#!/usr/bin/env python3
from gps3 import gps3
import time
import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

# create console handler and set level to info
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)



def main():
    connection = gps3.GPSDSocket()
    fix = gps3.Fix()

    try:
        for data in connection:
            if data:
                logger.info(data)
            else:
                pass

            time.sleep(1)

    except KeyboardInterrupt:
        connection.close()
        print("\nTerminated by user\nGood Bye.\n")


if __name__ == "__main__":
    main()
