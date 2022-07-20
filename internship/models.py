from django.db import models

# Create your models here.
class category(models.Model):
    categoryname=models.CharField(max_length=50)
   
class products(models.Model):
    categotyname=models.ForeignKey(category, default=1,on_delete=models.SET_DEFAULT,db_column='categoryname')
    product_name=models.CharField(max_length=50)
    price=models.IntegerField()
    quantity=models.IntegerField()
    description=models.CharField(max_length=50)

