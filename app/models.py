import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def profile_upload_path(instance, filename):
    return os.path.join('profile', str(instance.id), filename)

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(u"이름", max_length=64, blank=True, null=True)
    name_en = models.CharField(u"이름(EN)", max_length=64, blank=True, null=True)
    position = models.CharField(u"직책", max_length=64, blank=True, null=True)
    position_en = models.CharField(u"직책(EN)", max_length=64, blank=True, null=True)
    intro = models.TextField(u"소개", blank=True, null=True)
    intro_en = models.TextField(u"소개(EN)", blank=True, null=True)
    facebook_url = models.URLField(u"페이스북URL", blank=True, null=True)
    profile_image = models.ImageField(upload_to=profile_upload_path, blank=True, null=True)
    pub_date = models.DateTimeField(u"가입일", default=timezone.now)
    modified_date = models.DateTimeField(u"수정일", auto_now=True)

    def get_name(self, lang):
        if lang == 'ko-kr':
            return "%s (%s)" % (self.name, self.name_en)
        else:
            return self.name_en

    def get_position(self, lang):
        if lang == 'ko-kr':
            return self.position
        else:
            return self.position_en

    def get_intro(self, lang):
        if lang == 'ko-kr':
            return self.intro
        else:
            return self.intro_en

class Today(models.Model):
    title = models.CharField(u"타이틀", max_length=255)
    title_en = models.CharField(u"타이틀(EN)", max_length=255)
    is_active = models.BooleanField(u"활성화여부", default=True)
    display_order = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField(u"생성일", default=timezone.now)
    modified_date = models.DateTimeField(u"수정일", auto_now=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title

    def get_title(self, lang):
        if lang == 'ko-kr':
            return self.title
        else:
            return self.title_en

class TodayItem(models.Model):
    today = models.ForeignKey(Today)
    key_str = models.CharField("Key", max_length=255)
    key_str_en = models.CharField("Key(EN)", max_length=255, blank=True, null=True)
    value_str = models.CharField("Value", max_length=255, blank=True, null=True)
    value_str_en = models.CharField("Value(EN)", max_length=255, blank=True, null=True)
    value_link_url = models.CharField("Value link", max_length=255, blank=True, null=True)
    is_active = models.BooleanField(u"활성화여부", default=True)
    display_order = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField(u"생성일", default=timezone.now)
    modified_date = models.DateTimeField(u"수정일", auto_now=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.key_str

    def get_key_str(self, lang):
        if lang == 'ko-kr':
            return self.key_str
        else:
            return self.key_str_en

    def get_value_str(self, lang):
        if lang == 'ko-kr':
            return self.value_str
        else:
            return self.value_str_en

class Experience(models.Model):
    TYPE_CHOICES = (
        ('professional', u"Professional"),
        ('private', u"Private"),
        ('other', u"Education & Other"),
    )
    type = models.CharField(
        u"타입", max_length=20, choices=TYPE_CHOICES)
    start_date = models.DateTimeField(u"시작일")
    end_date = models.DateTimeField(u"종료일", blank=True, null=True)
    company = models.CharField(u"회사", max_length=255)
    company_en = models.CharField(u"회사(EN)", max_length=255, blank=True, null=True)
    company_link_url = models.CharField("회사 link", max_length=255, blank=True, null=True)
    is_active = models.BooleanField(u"활성화여부", default=True)
    display_order = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField(u"생성일", default=timezone.now)
    modified_date = models.DateTimeField(u"수정일", auto_now=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return "%s, %s, %s, %s" % (self.type, self.start_date, self.end_date, self.company)

    def get_company(self, lang):
        if lang == 'ko-kr':
            return self.company
        else:
            return self.company_en

class ExperienceItem(models.Model):
    experience = models.ForeignKey(Experience)
    key_str = models.CharField("Key", max_length=255)
    key_str_en = models.CharField("Key(EN)", max_length=255, blank=True, null=True)
    value_str = models.CharField("Value", max_length=255, blank=True, null=True)
    value_str_en = models.CharField("Value(EN)", max_length=255, blank=True, null=True)
    value_link_url = models.CharField("Value link", max_length=255, blank=True, null=True)
    is_active = models.BooleanField(u"활성화여부", default=True)
    display_order = models.PositiveIntegerField(default=0)
    parent = models.ForeignKey('self', blank=True, null=True)
    pub_date = models.DateTimeField(u"생성일", default=timezone.now)
    modified_date = models.DateTimeField(u"수정일", auto_now=True)

    def __str__(self):
        return self.key_str

    def get_value_str(self, lang):
        if lang == 'ko-kr':
            return self.value_str
        else:
            return self.value_str_en
    