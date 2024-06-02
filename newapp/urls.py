from django.urls import path
from newapp.apps import NewappConfig
from newapp.views import home, contact


app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact')
]
