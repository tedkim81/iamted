from django.contrib import admin
from app.models import Goal, GoalTask, Content

class GoalTaskInline(admin.StackedInline):
    model = GoalTask

class GoalAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_kr', 'display_order', 'crt_dt']
    inlines = [GoalTaskInline]

class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'crt_dt']

admin.site.register(Goal, GoalAdmin)
admin.site.register(Content, ContentAdmin)