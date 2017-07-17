from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import translation
from django.contrib.auth.models import User
from app.models import Today, MyUser, Experience, ExperienceItem

class ProfileView(TemplateView):
    template_name = "profile.html"

    def dispatch(self, request, *args, **kwargs):
        if 'lang' in request.GET:
            translation.activate(request.GET['lang'])
        return super(ProfileView, self).dispatch(request, *args, **kwargs)
