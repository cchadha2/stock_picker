import json

from pandas import DataFrame


def main():
    # Open response JSON file.
    with open("data/get_quotes.json") as response_file:
        response = json.load(response_file)

    # Process response.
    stock_table = DataFrame(response['quoteResponse']['result'])

    print(stock_table)


if __name__ == "__main__":
    main()
