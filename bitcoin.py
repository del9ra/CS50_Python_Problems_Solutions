import sys
import json
import requests

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    bitcoin = o["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    pass

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
else:
    try:
        x = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    p = bitcoin*float(sys.argv[1])
    print(f"${p:,.4f}")
