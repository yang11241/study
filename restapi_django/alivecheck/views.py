from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    response_data = {'resultCode': 200, 'message': '', 'resultData': ''}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

