#!/usr/bin/env python3
from gps3 import gps3
import time
import logging
import os
import datetime
import time

logger = logging.getLogger(__name__)
output_dir = os.path.dirname(os.path.realpath(__file__))
filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + "_gps.log"

logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

handler = logging.FileHandler(os.path.join(output_dir, filename), "w", encoding=None)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
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

            time.sleep(0.2)

    except KeyboardInterrupt:
        connection.close()
        logger.info("\nTerminated by user\nGood Bye.\n")


if __name__ == "__main__":
    main()
