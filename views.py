# -*- encoding:utf8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
import json
from django.db import connection as con

def main(req):
    return render(req, 'main.html')

def test(req):
    return render(req, 'test.html')


def exprn_vilages_view(req):
    global con
    cur=con.cursor()
    
    cur.execute('SELECT * FROM ExprnVilages;')
    print cur._executed
    RESULT=cur.fetchall()
    
    return render(req, 'exprn_vilages_view.html',
                  {'TITLE':'체험마을',
                   'RESULT':RESULT,
                   })
def exprn_vilage_history(req):
    return render(req, 'exprn_vilage_history_view.html')





