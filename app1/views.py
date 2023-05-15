from typing import Any, Dict
from django.shortcuts import render
from app1.forms import *
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.

class Template_view(TemplateView):
    template_name='template_view.html'
    def get_context_data(self, **kwargs):
        T=TopicForm()
        co= super().get_context_data(**kwargs)
        
        co['T']=T
        return co
    def post(self,request):
        TO=TopicForm(request.POST)
        if TO.is_valid():
            TO.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('data is not correct')