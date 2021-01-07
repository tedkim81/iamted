from django.db import models
from datetime import datetime

class Goal(models.Model):
    title_kr = models.CharField(u'목표명(한글)', max_length=100)
    title_en = models.CharField(u'목표명(영어)', max_length=100)
    goal_status_kr = models.TextField(u'목표 상태(한글)')
    goal_status_en = models.TextField(u'목표 상태(영어)')
    curr_status_kr = models.TextField(u'현재 상태(한글)')
    curr_status_en = models.TextField(u'현재 상태(영어)')
    goal_point = models.PositiveIntegerField(u'목표 포인트')
    display_order = models.PositiveIntegerField(u'노출 순서', default=0)
    crt_dt = models.DateTimeField(u'등록일', auto_now_add=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title_kr

    def get_achievement_percent(self):
        percent = 0
        for gt in self.goaltask_set.all():
            percent += gt.get_contribute_percent()
        return round(percent, 1)

class GoalTask(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    title_kr = models.CharField(u'과제명(한글)', max_length=100)
    title_en = models.CharField(u'과제명(영어)', max_length=100)
    task_dt = models.DateField(u'과제수행일')
    task_point = models.PositiveIntegerField(u'과제 포인트')
    remembered_years = models.PositiveIntegerField(u'기억기간(years)', default=10)
    link_url = models.URLField(u'관련 링크', blank=True, null=True)
    crt_dt = models.DateTimeField(u'등록일', auto_now_add=True)

    class Meta:
        ordering = ['-task_dt', '-id']

    def __str__(self):
        return self.title_kr

    def get_past_years(self):
        return round((datetime.now().date() - self.task_dt).days / 365, 1)

    def get_contribute_percent(self):
        years_diff = self.remembered_years - self.get_past_years()
        if years_diff > 0:
            return round(self.task_point * (years_diff / self.remembered_years) / self.goal.goal_point * 100, 1)
        else:
            return 0

class Content(models.Model):
    type = models.CharField(u'타입', max_length=50)
    content_kr = models.TextField(u'내용(한글)')
    content_en = models.TextField(u'내용(영어)')
    crt_dt = models.DateTimeField(u'등록일', auto_now_add=True)
