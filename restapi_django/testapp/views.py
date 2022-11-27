from django.shortcuts import render

from django.http import HttpResponse
from .models import TestClass

def index(request):
    category_list = TestClass.objects.all()
    context = {'category_list': category_list}
    return render(request, 'testapp/index.html', context)
