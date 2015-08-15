#!/usr/bin/env python
# coding=utf-8
from django.contrib import admin
from shaoyaheng.models import UserProfile, Page, Result

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('number', 'age', 'gender', 'grade', 'major', )
    search_fields = ('number', )
    fieldsets = (
        (
            None,
            {
                'fields': ('number', 'age', 'gender', 'grade', 'major', )
            }
        ),
    )

class PageAdmin(admin.ModelAdmin):
    list_display = ('page_num', 'page_type', 'content', 'next_page' )
    fieldsets = (
        (
            None,
            {
                'fields': ('page_num', 'page_type', 'content', 'next_page' )
            }
        ),
    )

class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'result' )
    search_fields = ('user', )
    fieldsets = (
        (
            None,
            {
                'fields': ('user', 'result' )
            }
        ),
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Result, ResultAdmin)
