
from django.conf.urls import url, include

from . import views
urlpatterns = [
 
    url(r'^$', views.index, name = 'index'),
	url(r'^(?P<table_id>[0-9]+)/$', views.dataset_table, name = 'dataset_table'),
    
] 
