# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Size
# Create your views here.
#class index(TemplateView):
 #template_name="index.html"
def index(request):
   #html=""
   #all_values=Size.objects.all()
   #for value in all_values:
    # html+='<a href=/app/'+value.name+'>'+value.name+'</a></br>'
   #return HttpResponse(html)
   all_values=Size.objects.all()
   context={'all_values':all_values}
   return render(request,'index.html',context)
def detail(request,shirt_size):
   return HttpResponse("<h2>size:"+shirt_size+"</h2>")
 

