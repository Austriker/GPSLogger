#!/usr/bin/env python3
from gps3 import gps3
import time
import logging

logger = logging.getLogger(__name__)

handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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
