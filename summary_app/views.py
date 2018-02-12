# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from geospaas.catalog.models import Dataset

# Create your views here.

def dataset_table(request, table_id):
    dataset = Dataset.objects.get(pk = table_id)
    context = {'dataset': dataset}
    return render(request,'summary_app/dataset_table.html',context)

def detail(request, table_id):
     return HttpResponse("You are looking at table %s.", table_id)


def index(request):
    datasets = Dataset.objects.all()
    context = {'datasets': datasets}
    return render (request, 'summary_app/index.html', context)
