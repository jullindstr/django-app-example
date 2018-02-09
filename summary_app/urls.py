
from django.conf.urls import url, include

from . import views
urlpatterns = [
 
    url(r'^$', views.dataset_table, name = 'dataset_table'),
    
    
] 
