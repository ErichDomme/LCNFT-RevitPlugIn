# API_KEY = "23FFET6VUG68K6YVED9RF6P79BAU8KV4ZV"

from pyrevit import forms
import clr
import json

clr.AddReference("System")
from System.Net import WebClient

# Define function to fetch Ethereum info
def get_ethereum_info():
    API_KEY = "23FFET6VUG68K6YVED9RF6P79BAU8KV4ZV"
    ETH_PRICE_URL = (
        "https://api.etherscan.io/api?module=stats&action=ethprice&apikey={}".format(
            API_KEY
        )
    )
    GAS_PRICE_URL = "https://api.etherscan.io/api?module=proxy&action=eth_gasPrice&apikey={}".format(
        API_KEY
    )

    with WebClient() as client:
        eth_price_response = json.loads(client.DownloadString(ETH_PRICE_URL))
        gas_price_response = json.loads(client.DownloadString(GAS_PRICE_URL))

    eth_price = float(eth_price_response["result"]["ethusd"])
    gas_price_wei = int(gas_price_response["result"], 16)  # Convert hex to int
    gas_price_gwei = gas_price_wei / 10 ** 9  # Convert wei to gwei

    return eth_price, gas_price_gwei


# Fetch the info
eth_price, gas_price = get_ethereum_info()

# Display the results
message = "Ethereum Price: ${}\nGas Price: {} Gwei".format(eth_price, gas_price)
forms.alert(message, title="Ethereum Info", ok=True, warn_icon=True)
