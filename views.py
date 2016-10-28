# -*- encoding:utf8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
import json

def main(req):
    
    return render(req, 'main.html')

