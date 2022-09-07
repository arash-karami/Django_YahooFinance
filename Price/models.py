from django.db import models

# Create your models here.


class Ticker(models.Model):
    
    ticker= models.CharField(max_length=50)


    def __str__(self):
        return self.ticker

class Data(models.Model):
    
    name= models.ForeignKey(Ticker , on_delete=models.CASCADE , related_name='named')
    price = models.DecimalField( max_digits=5, decimal_places=2)
    date = models.IntegerField( blank=True , null=True )


    def __str__(self):
        
            return "%s %s %s" % (self.price , self.date , self.name_id)  

    