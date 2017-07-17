from django.contrib import admin
from app.models import MyUser, Today, TodayItem, Experience, ExperienceItem

admin.site.register(MyUser)
admin.site.register(Today)
admin.site.register(TodayItem)
admin.site.register(Experience)
admin.site.register(ExperienceItem)
