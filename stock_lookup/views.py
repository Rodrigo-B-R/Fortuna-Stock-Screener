from django.shortcuts import render

from django.http import HttpResponse
from .api_client import *
import json

# Create your views here.


# stock_info_key= 'S3TLXSQ7JZXX0F4Z' #https://www.alphavantage.co/
# stock_images_key= 'Wmx2eCtCpSi2OFVVGEvq/w==59m4O4LX9tv2uXs5' #https://api-ninjas.com/api/animals

def cashflow_to_chart(cashflow_data):
    annual_reports= cashflow_data['annualReports']
    labels=[]
    free_cashflow=[]
    dividends= []

    for year in annual_reports:

        year_fcf= float(year['operatingCashflow']) - float(year['capitalExpenditures'])
        if 'dividendPayout' in year:
            dividends.append(year['dividendPayout'])
        else: dividends.append(0)

        labels.append(year["fiscalDateEnding"][:4])
        free_cashflow.append(year_fcf)
    
    labels.reverse()
    free_cashflow.reverse()
    dividends.reverse()

    free_cashflow_chart= {'labels':labels, 'free_cashflow': free_cashflow, 'dividends':dividends}

    quarterly_reports= cashflow_data["quarterlyReports"]
    dividends_quarter=[]
    labels_quarter=[]
    free_cashflow_quarter=[]

    for quarter in quarterly_reports:
        quarter_fcf= float(quarter['operatingCashflow']) - float(quarter['capitalExpenditures'])
        if 'dividendPayout' in quarter:
            dividends_quarter.append(quarter['dividendPayout'])
        else: dividends_quarter.append(0)

        labels_quarter.append(quarter["fiscalDateEnding"][:7])
        free_cashflow_quarter.append(quarter_fcf)

    labels_quarter.reverse()
    free_cashflow_quarter.reverse()
    dividends_quarter.reverse()

    fcf_quarter_chart={'labels':labels_quarter,
                       'free_cashflow': free_cashflow_quarter, 
                       'dividends':dividends_quarter}


    return free_cashflow_chart, fcf_quarter_chart

def eps_to_chart(eps):
    annual_Earnings= eps['annualEarnings']
    labels=[]
    eps_anual=[]

    for year in annual_Earnings:

        

        labels.append(year["fiscalDateEnding"][:4])
        eps_anual.append(float(year['reportedEPS']))
    
    labels.reverse()
    eps_anual.reverse()

    eps_chart= {'labels':labels, 'eps': eps_anual}
    
    

    quarterly_Earnings = eps['quarterlyEarnings']
    
    labels_quarter=[]
    earnings_quarter=[]

    for quarter in quarterly_Earnings:
        labels_quarter.append(quarter['fiscalDateEnding'][:7])
        earnings_quarter.append(quarter['reportedEPS'])

    labels_quarter.reverse()
    earnings_quarter.reverse()

    eps_quarter_chart={'labels': labels_quarter, 'earnings':earnings_quarter}




    return eps_chart, eps_quarter_chart

def incomestatement_to_chart(incomestatement):
    annual_reports= incomestatement['annualReports']
    labels=[]
    revenue=[]
    ebitda=[]
    net_income=[]
    expenses= []

    for year in annual_reports:

        year_expense= float(year['totalRevenue']) - float(year['operatingIncome'])

        expenses.append(year_expense)

        revenue.append(year['totalRevenue'])
        net_income.append(year['netIncome'])
        ebitda.append(year['ebitda'])
        labels.append(year["fiscalDateEnding"][:4])
        
    
    labels.reverse()
    revenue.reverse()
    net_income.reverse()
    expenses.reverse()
    ebitda.reverse()

    incomestatement_chart = {'labels': labels, 'revenue': revenue, 'net_income': net_income, 'ebitda': ebitda, 'expenses': expenses}
    
    quarterly_reports= incomestatement['quarterlyReports']
    labels_quarter=[]
    revenue_quarter=[]
    net_income_quarter=[]
    ebitda_quarter=[]
    expenses_quarter=[]

    for quarter in quarterly_reports:

        quarter_expense= float(quarter['totalRevenue']) - float(quarter['operatingIncome'])

        expenses_quarter.append(quarter_expense)

        revenue_quarter.append(quarter['totalRevenue'])
        net_income_quarter.append(quarter['netIncome'])
        ebitda_quarter.append(quarter['ebitda'])
        labels_quarter.append(quarter["fiscalDateEnding"][:7])
    
    labels_quarter.reverse()
    revenue_quarter.reverse()
    net_income_quarter.reverse()
    ebitda_quarter.reverse()
    expenses_quarter.reverse()

    incomestatement_chart_quarter={'labels':labels_quarter, 
                                   'revenue': revenue_quarter, 
                                   'net_income': net_income_quarter,
                                   'ebitda':ebitda_quarter,
                                   'expenses':expenses_quarter}



    
    
    return incomestatement_chart, incomestatement_chart_quarter


def home(request):

    return render(request,'stock_lookup/home.html')




def stock_view(request):
    
    ticker = request.GET.get('ticker','').upper()

    overview_data= get_overview(ticker)
    image= get_image(ticker)
    cashflow_chart, cashflow_chart_quarter = cashflow_to_chart(get_cashflow(ticker))
    eps_chart, eps_chart_quarter= eps_to_chart(get_eps(ticker)) 
    incomestatement_chart, incomestatement_chart_quarter= incomestatement_to_chart(get_incomestatement(ticker))


    

    return render(request, 'stock_lookup/stock_view_page.html',
                  {'overview_data': overview_data,
                   'image': image,
                    'cashflow_chart': json.dumps(cashflow_chart),
                      'eps_chart': json.dumps(eps_chart), 
                      'incomestatement_chart': json.dumps(incomestatement_chart), 
                      'cashflow_chart_quarter':json.dumps(cashflow_chart_quarter),
                      'eps_chart_quarter': json.dumps(eps_chart_quarter),
                      'incomestatement_chart_quarter': json.dumps(incomestatement_chart_quarter)} 
                          )
    

def error_view(request):

    return render(request,'stock_lookup/error.html')


