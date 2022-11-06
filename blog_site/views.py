from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

def Index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list')) 

# App_Blog:blog_list means  app_name = 'App_Blog' and url name='blog_list'