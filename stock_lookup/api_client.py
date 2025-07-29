import requests
from django.shortcuts import redirect
from django.conf import settings 




stock_info_key= settings.STOCK_INFO_KEY #https://www.alphavantage.co/
stock_images_key= settings.STOCK_IMAGES_KEY #https://api-ninjas.com/api/animals

def get_overview(ticker):

   
    overview_url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={stock_info_key}'
    
   
    overview_response=make_api_call(overview_url)
        
    overview_data = overview_response.json()

    
    
    return overview_data

def get_cashflow(ticker):
    cashflow_url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={ticker}&apikey={stock_info_key}'
    cashflow_response = make_api_call(cashflow_url)

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
    response = make_api_call(url)
    eps = response.json()

    return eps

def get_incomestatement(ticker):
    url=f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey={stock_info_key}'
    response=make_api_call(url)
    incomestatement=response.json()
    return incomestatement



def make_api_call(url):
    try:
        response = requests.get(url)
    except requests.exceptions.HTTPError:
        return redirect('error')
    return response