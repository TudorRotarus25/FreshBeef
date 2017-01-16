# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from models import Article


class LayoutView(View):
    pass


class HomepageView(ListView, LayoutView):
    model = Article
    template_name = 'news/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        return context
