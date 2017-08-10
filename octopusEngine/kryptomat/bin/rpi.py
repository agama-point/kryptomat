import argparse
import logging

parser = argparse.ArgumentParser(
    description='A BTC/LTC Rapsberry Pi automat.'
)
parser.add_argument("-v", "--debug", help="increase output verbosity",
                    action="store_true")

logger = logging.getLogger(__name__)

def main():
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug('Debug mode enabled.')
    # ###### REAL CODE STARTS HERE !! ######

    print("IT WORKS!!")
