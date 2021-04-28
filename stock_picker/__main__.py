#!usr/bin/env python3
import argparse
import os

from stock_picker import start_picker

parser = argparse.ArgumentParser()
parser.add_argument("api_key")
parser.add_argument("region")
parser.add_argument("symbols")

params = parser.parse_args()
api_key = params.api_key
delattr(params, "api_key")

start_picker(api_key=api_key, params=vars(params))
