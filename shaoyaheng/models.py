#!/usr/bin/env python
# coding=utf-8
from django.db import models
from django import forms
from django.utils.translation import ugettext as _

class UserProfile(models.Model):
    number  = models.IntegerField(
        verbose_name = _(u'编号'),
        help_text = _(u' ')
    )
    age  = models.IntegerField(
        verbose_name = _(u'年龄'),
        help_text = _(u' ')
    )
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, _(u'男')),
        (FEMALE, _(u'女')),
    )
    gender = models.CharField(
        verbose_name = _(u'性别'),
        help_text = _(u' '),
        max_length = 2,
        choices = GENDER_CHOICES,
        default = MALE
    )
    grade = models.CharField(
        verbose_name = _(u'年级'),
        help_text = _(u' '),
        max_length = 255
    )
    major = models.CharField(
        verbose_name = _(u'专业'),
        help_text = _(u' '),
        max_length = 255
    )
    def __unicode__(self):
        return u'%d' % self.number

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
            'number' : forms.NumberInput(attrs={'class':'form-control'}),
            'age' : forms.NumberInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-control'}),
            'grade' : forms.TextInput(attrs={'class':'form-control'}),
            'major' : forms.TextInput(attrs={'class':'form-control'}),
        }
        fields = '__all__'

class Page(models.Model):
    page_num = models.IntegerField(
        verbose_name = _(u'页码'),
        help_text = _(u' ')
    )
    INFO = 'I'
    QUIZ = 'Q'
    PAGE_TYPE_CHOICES = (
        (INFO, _(u'说明')),
        (QUIZ, _(u'测试')),
    )
    page_type = models.CharField(
        verbose_name = _(u'页面类型'),
        help_text = _(u' '),
        max_length = 2,
        choices = PAGE_TYPE_CHOICES,
        default = INFO
    )
    content = models.TextField(
        verbose_name = _(u'消息'),
        help_text = _(u' ')
    )
    next_page = models.CharField(
        verbose_name = _(u'下一页'),
        help_text = _(u' '),
        max_length = 255
    )
    def __unicode__(self):
        return u'%d %s' % (self.page_num, self.content)

class Result(models.Model):
    user = models.OneToOneField(
        UserProfile,
        verbose_name = _(u'被测试者')
    )
    result = models.TextField(
        verbose_name = _(u'测试结果'),
        help_text = _(u' ')
    )
    def __unicode__(self):
        return u'%s %s' % (self.user, self.result)
