from django.db import models
from django.contrib.auth.models import User


# Create your models here.




class Portofolio(models.Model):
    portofolio_name= models.CharField(max_length=30)
    positions= models.JSONField(default=dict)
    
    owner=models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='owner of the portafolio')



    def addPosition(self, stock_ticker, quantity,price):
        
        stock_and_price= (quantity, price)
        
        self.positions[stock_ticker]= stock_and_price
        
    
    def initial_value(self):
        initial_value= sum( quantity* price for quantity, price in self.positions.values())
        return initial_value
    



    
    

        
        
