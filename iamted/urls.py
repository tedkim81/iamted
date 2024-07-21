"""iamted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from app import views
from mytube import apis

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.ProfileView.as_view(), name='profile'),
    url(r'^health-check/', views.health_check, name='health-check'),
    url(r'^goal_modal/(?P<pk>\d+)/$', views.GoalModalView.as_view(), name='goal-modal'),
    url(r'^mytube/api/recommend_words$', apis.recommend_words, name='mytube-api-recommend-words'),
    url(r'^mytube/api/search$', apis.search, name='mytube-api-search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]