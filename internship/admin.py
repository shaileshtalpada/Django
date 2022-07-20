from django.contrib import admin
from .models import products
from .models import category
# Register your models here.
class c_display(admin.ModelAdmin):
     list_displays=('categoryname')
    
      
       
admin.site.register(category,c_display)
  
class p_display(admin.ModelAdmin):
     list_displayy=('categoryname','product_name','price','quantity','description')
    
      
        

admin.site.register(products,p_display)