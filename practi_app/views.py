from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from practi_app.forms import my_form
from django import forms
from django.views.generic.edit import FormView
# Create your views here.


class Index(TemplateView):
    template_name = 'practi_app/index.html'


class new_form(FormView):
    template_name = 'practi_app/forms.html'



    def get(self,reqeust):
        form = FormView()
        return render(request,self.template_name,{'form':form})
