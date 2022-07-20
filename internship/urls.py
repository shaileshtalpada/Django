
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name="indexfile"),
    path('aboutus',views.about,name="aboutusfile"),
    path('sports',views.sportss,name="sports"),
    path('entrs',views.entr,name="entfile"),
    path('national',views.nati,name="nationalfile"),
    path('politics',views.poli,name="politicsfile"),
    path('worlds',views.wor,name="worldfile"),
    path('tachno',views.tech,name="techfile"),
    path('bus',views.bus,name="busfile"),
    path('start',views.start,name="startfile"),
    path('misce',views.misce,name="miscellaneousfile"),
    path('hatke',views.hatke,name="hatkefile"),
    path('auto',views.auto,name="autofile"),
    path('sci',views.sci,name="sciencefile"),
   
    
]
