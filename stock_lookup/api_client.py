import requests
from django.shortcuts import redirect
from django.conf import settings
from .client import make_api_call_via_proxy






stock_info_key= settings.STOCK_INFO_KEY #https://www.alphavantage.co/
stock_images_key= settings.STOCK_IMAGES_KEY #https://api-ninjas.com/api/animals


def get_overview(ticker):


   
    overview_url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}'
   
   
    overview_response=make_api_call(overview_url)


    return overview_response
       
   




def get_cashflow(ticker):
    cashflow_url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={ticker}'
    cashflow_response = make_api_call(cashflow_url)


    return cashflow_response


   
   


def get_image(ticker):
    url_image= f'https://api.api-ninjas.com/v1/logo?ticker={ticker}'
    image_response = requests.get(url_image, headers={'X-Api-Key': f'{stock_images_key}'})
    image_json = image_response.json()
    image= image_json[0]
    return image


def get_eps(ticker):
    url= f'https://www.alphavantage.co/query?function=EARNINGS&symbol={ticker}'
    response = make_api_call(url)
    return response
   
    return eps


def get_incomestatement(ticker):
    url=f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}'
    response=make_api_call(url)
    return response
 




def make_api_call(url):
    data= make_api_call_via_proxy(url)
    return data

