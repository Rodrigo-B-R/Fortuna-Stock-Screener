import requests
import json

# The URL of your Node.js proxy server.
# If your Python script is running on a different machine,
# replace 'localhost' with the IP address or hostname of the server running the proxy.

# The URL of your Node.js proxy server.
PROXY_URL = 'http://localhost:3000/api/alpha-vantage'

def make_api_call_via_proxy(alpha_vantage_url):
    """
    Makes a request to the proxy server, passing the target Alpha Vantage URL.

    Args:
        alpha_vantage_url (str): The target URL for the Alpha Vantage API
                                 (without the API key).

    Returns:
        dict: The JSON data from the API, or None if an error occurred.
    """
    # The proxy expects the target URL in a query parameter named 'url'.
    params = {'url': alpha_vantage_url}
    
    print(f"--> Calling proxy at: {PROXY_URL}")
    print(f"--> with params: {params}")

    try:
        # The `requests` library will correctly encode the params, resulting in a call to:
        # http://localhost:3000/api/alpha-vantage?url=https%3A%2F%2Fwww.alphavantage.co%2F...
        response = requests.get(PROXY_URL, params=params)

        # This will raise an exception for HTTP error codes (4xx or 5xx)
        response.raise_for_status()

        print("--> Request successful!")
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        try:
            print(f"Error details from server: {response.json()}")
        except json.JSONDecodeError:
            print(f"Could not decode JSON from error response: {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"A request error occurred: {req_err}")

    return None


