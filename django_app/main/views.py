from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class MenuItemView(TemplateView):
    template_name = 'base.html'

