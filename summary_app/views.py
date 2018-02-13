# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from geospaas.catalog.models import Dataset

class DatasetView(generic.DetailView):
    model = Dataset
    template_name = 'summary_app/dataset_table.html'
	

class IndexView(generic.ListView): 	 
    context_object_name = 'datasets'
    template_name = 'summary_app/index.html'
    
    def get_queryset(self):
        return Dataset.objects.all()
	 
