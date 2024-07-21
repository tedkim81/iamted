from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import translation
from app.models import Goal, Content
from django.views.generic import DetailView

def health_check(request):
    return HttpResponse(status=200)

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def dispatch(self, request, *args, **kwargs):
        if 'lang' in request.GET:
            translation.activate(request.GET['lang'])
            self.lang = request.GET['lang']
        else:
            self.lang = 'ko'
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['goals'] = Goal.objects.all().prefetch_related('goaltask_set')
        for c in Content.objects.all():
            if self.lang == 'en':
                context[c.type] = c.content_en
            else:
                context[c.type] = c.content_kr
        return context

class GoalModalView(DetailView):
    model = Goal
    template_name = 'goal_modal.html'

    def dispatch(self, request, *args, **kwargs):
        if 'lang' in request.GET:
            translation.activate(request.GET['lang'])
        return super(GoalModalView, self).dispatch(request, *args, **kwargs)
