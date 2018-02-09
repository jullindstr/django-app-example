# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from geospaas.catalog.models import Dataset

# Create your views here.

def dataset_table(request):
    datasets = Dataset.objects.all()
    context = {'datasets': datasets}
    return render(request,'summary_app/dataset_table.html',context = context)


