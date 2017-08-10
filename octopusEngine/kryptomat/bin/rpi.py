import argparse
import logging

parser = argparse.ArgumentParser(
    description='A BTC/LTC Rapsberry Pi automat.'
)
parser.add_argument("-v", "--debug", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-qr", "--qr-code-output-path",
                    help="The path where to generate QR code. Default: qrcode.png",
                    default="qrcode.png")

logger = logging.getLogger(__name__)

def main():
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug('Debug mode enabled.')
    # ###### REAL CODE STARTS HERE !! ######

    print("IT WORKS!!")
    print("QR code output path is %s" % args.qr_code_output_path)
