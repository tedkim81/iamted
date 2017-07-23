from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import translation

class ProfileView(TemplateView):
    template_name = "profile.html"

    def dispatch(self, request, *args, **kwargs):
        if 'lang' in request.GET:
            translation.activate(request.GET['lang'])
        return super(ProfileView, self).dispatch(request, *args, **kwargs)
