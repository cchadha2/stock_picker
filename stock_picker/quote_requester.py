import json
import os

import requests

import yaml


def quote_getter(url, host, params, api_key):
    return requests.get(url,
                        headers={'x-rapidapi-host': host, 'x-rapidapi-key': api_key},
                        params=params).json()


def main():
    # Load config file.
    with open("config.yml", "rt") as config_file:
        config = yaml.full_load(config_file)

    # GET quote response payload.
    response = quote_getter(url=config["endpoint"],
                            host=config["host"],
                            api_key=config["api_key"],
                            params=config["params"])

    # Dump response JSON to file.
    with open(os.path.join("data", config["output_file"]), "wt") as output_file:
        json.dump(response, output_file)


if __name__ == "__main__":
    main()
