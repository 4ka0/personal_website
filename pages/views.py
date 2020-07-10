
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

def set_language(request, current_lang_code):
    '''
    Function to set the display language, selected by the user.
    '''
    if current_lang_code == "en":
        new_lang_code = "ja"
        new_lang = "Japanese"
    else:
        new_lang_code = "en"
        new_lang = "English"
    return render(request, 'home.html', { 'new_lang_code': new_lang_code },
                                        { 'new_lang': new_lang })