from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class TranslationPageView(TemplateView):
    template_name = 'translation.html'

class CodingPageView(TemplateView):
    template_name = 'coding.html'

class BlogPageView(TemplateView):
    template_name = 'blog.html'
