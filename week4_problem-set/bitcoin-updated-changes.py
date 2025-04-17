import sys
import requests
import json
from requests import RequestException

def main():

    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)

    API_TOKEN = "b97d273322d4e65d56e4b639c92a42c6a1ea6a40389ca9256a613951b493b982"
    try:
        bitcoin_number = float(sys.argv[1])
        # url = "https://rest.coincap.io/v3/assets"
        # headers = {
        #     "Content-Type":"application/json",
        #     "token_type": f"Bearer {API_TOKEN}",
        # }
        # response = requests.get(url,headers=headers)
        bitcoin_price = None
        response = requests.get("https://rest.coincap.io/v3/assets",{"apiKey":API_TOKEN})
        response.raise_for_status()


    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    except RequestException:
        print("Error occurred")
        sys.exit(1)

    else:
        data = response.json()
        bitcoin_price = float(data["data"][0]["priceUsd"])



        amount = bitcoin_price * bitcoin_number
        print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()







