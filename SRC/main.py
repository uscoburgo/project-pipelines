import os 
import sys
from argparse import ArgumentParser
#import subprocess
from create_output import CreateReport


def main():
    parser = ArgumentParser(description="This program shows the sentiment for a specific stock trading in the S&P500, and provides info on the price of the stock")
    parser.add_argument("-s","--stock",help="flag: show the data related to a specific stock. Enter the ticker/symbol e.g. Apple would be 'AAPL')",default=None)

    args = parser.parse_args()
    #print(args)

    print(CreateReport(args.stock))

if __name__ == "__main__":
    main()