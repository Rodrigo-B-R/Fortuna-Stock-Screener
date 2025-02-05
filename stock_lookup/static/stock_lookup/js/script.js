let fcf_barChart = new Chart(FCF_document,
    {type: 'bar',
    
    data: {
        labels: fcf_labels,
        datasets: [{
            label: 'Free Cash Flow(USD)',
            data: fcf_data,
            backgroundColor: 'rgba(242, 121, 53, 1)',
            hoverBorder: 3,
            hoverColor: 'rgba(242, 121, 53, 1)'
            }]
                         },
    options: shared_options
               
    
       }
)


const eps_chartData= JSON.parse('{{ eps_chart|escapejs }}')
const eps_labels= eps_chartData.labels
const eps_data= eps_chartData.eps
let EPS_document = document.getElementById('EPS_chart').getContext('2d');

let eps_barchart = new Chart(EPS_document, {type: 'bar',
    
    data: {
        labels: eps_labels,
        datasets: [{
            label: 'EPS(USD)',
            data: eps_data,
            backgroundColor: 'rgba(255, 240, 0, 1)',
            hoverBorder: 3,
            hoverColor: 'rgba(255, 240, 0, 1)'
            }]
                         },
    options:shared_options
    
       }
)
const incomestatement_chartData = JSON.parse('{{ incomestatement_chart|escapejs }}')
const  is_labels= incomestatement_chartData.labels
const revenue= incomestatement_chartData.revenue
const net_income= incomestatement_chartData.net_income
const ebitda= incomestatement_chartData.ebitda
const expenses= incomestatement_chartData.expenses

let revenue_document = document.getElementById('Revenue_Chart').getContext('2d');

let revenue_chart = new Chart(revenue_document,
    {type: 'bar',
    
    data: {
        labels: is_labels,
        datasets: [{
            label: 'Revenue(USD)',
            data: revenue,
            backgroundColor: 'rgba(255,179,67)',
            hoverBorder: 3,
            hoverColor: 'rgba(255,179,67)'
            }]
                         },
    options: shared_options
    
       }
)
let net_income_document =document.getElementById('Net_Income_Chart').getContext('2d');

let net_income_chart = new Chart(net_income_document,
    {type: 'bar',
    
    data: {
        labels: is_labels,
        datasets: [{
            label: 'Net Income(USD)',
            data: net_income,
            backgroundColor: 'rgba(102,241,194)',
            hoverBorder: 3,
            hoverColor: 'rgba(102,241,194)'
            }]
                         },
    options: shared_options
    
       }
)

let ebitda_document= document.getElementById('Ebitda_Chart').getContext('2d')

let ebitda_chart = new Chart(ebitda_document,
    {type: 'bar',
    
    data: {
        labels: is_labels,
        datasets: [{
            label: 'EBITDA',
            data: ebitda,
            backgroundColor: 'rgba(144,213,255)',
            hoverBorder: 3,
            hoverColor: 'rgba(144,213,255)'
            }]
                         },
    options: shared_options
    
       }
)
let expenses_document= document.getElementById('Expenses_Chart').getContext('2d')
let expenses_chart = new Chart(expenses_document,
    {type: 'bar',
    
    data: {
        labels: is_labels,
        datasets: [{
            label: 'Expenses (USD)',
            data: expenses,
            backgroundColor: 'rgba(248, 131, 121)',
            hoverBorder: 3,
            hoverColor: 'rgba(248, 131, 121)'
            }]
                         },
    options: shared_options
    
       }
)
let dividends_document = document.getElementById('Dividends_Chart').getContext('2d');
let dividends_chart = new Chart(dividends_document,
    {type: 'bar',
    
    data: {
        labels: is_labels,
        datasets: [{
            label: 'Dividend (USD)',
            data: dividends,
            backgroundColor: 'rgba(200, 247, 197, 1)',
            hoverBorder: 3,
            hoverColor: 'rgba(200, 247, 197, 1)'
            }]
                         },
    options: shared_options


    
       }
       
)




// callback : function(value)
//                                 { if (value >= 1000000000 || value  <= -1000000000) {
//                                     return '$' + (value / 1000000000 ).toFixed(0) + 'b'; }
//                                 else if (value >= 1000000 || value <= -1000000) {
//                                     return '$' + (value / 1000000).toFixed(0) + 'm'; 
//                                 } else if (value >= 1000 || value<= -1000) {
//                                     return '$' + (value / 1000).toFixed(0) + 'k'; 
//                                 } else {
//                                     return  '$' + value; }
                                    
//                                     }