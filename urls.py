# -*- encoding:utf8 -*-
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.main, name='main'),
    url(r'^test$',views.test, name='test'),
    
    url(r'^exprnvilages$',views.exprn_vilages_view, name='exprn_vilages_view'),
    url(r'^exprn_vilage_history$',views.main, name='main'),
    
    

    
]
