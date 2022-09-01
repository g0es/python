#!/usr/bin/env python3
import sys, os, logging, logging.handlers
logpath='./Somelog.log'
app_name='application'

def main():
    logger.warning("this is a warning")

if __name__ == '__main__':
    try:
        # Init Logging
        logging.root.setLevel(logging.NOTSET)
        logger = logging.getLogger(app_name)
        # Init File Logger
        #ff = logging.Formatter('%(asctime)s %(name)s, %(levelname)s: %(message)s')
        #fh = logging.FileHandler(logpath)
        #fh.setLevel(logging.DEBUG)
        #fh.setFormatter(ff)
        #logger.addHandler(fh)

        # create console handler with a higher log level
        cf = logging.Formatter('%(levelname)s: %(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(cf)
        logger.addHandler(ch)

        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)