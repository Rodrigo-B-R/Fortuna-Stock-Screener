import requests


stock_info_key= 'S3TLXSQ7JZXX0F4Z' #https://www.alphavantage.co/
stock_images_key= 'Wmx2eCtCpSi2OFVVGEvq/w==59m4O4LX9tv2uXs5' #https://api-ninjas.com/api/animals


def get_overview(ticker):
    overview_url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={stock_info_key}'
    overview_response = requests.get(overview_url)
    overview_data = overview_response.json()

    
    
    return overview_data

def get_cashflow(ticker):
    cashflow_url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={ticker}&apikey={stock_info_key}'
    cashflow_response = requests.get(cashflow_url)
    cashflow_data = cashflow_response.json()
    

    return cashflow_data

    

def get_image(ticker):
    url_image= f'https://api.api-ninjas.com/v1/logo?ticker={ticker}'
    image_response = requests.get(url_image, headers={'X-Api-Key': f'{stock_images_key}'})
    image_json = image_response.json()
    image= image_json[0]
    return image

def get_eps(ticker):
    url= f'https://www.alphavantage.co/query?function=EARNINGS&symbol={ticker}&apikey={stock_info_key}'
    response = requests.get(url)
    eps = response.json()

    return eps

def get_incomestatement(ticker):
    url=f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey={stock_info_key}'
    response=requests.get(url)
    incomestatement=response.json()
    return incomestatement