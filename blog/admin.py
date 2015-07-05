#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Julia Wallmüller'

from django.contrib import admin
from django.db import models
from redactor.widgets import AdminRedactorEditor

from models import Post, Comment, Page, Category


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    fieldsets = [
        ('Details', {'fields': ['author', 'email', 'url', 'body', 'published'], 'classes': ['collapse']}),
    ]


class PostAdmin(admin.ModelAdmin):
    exclude = ['author']
    formfield_overrides = {
        models.TextField: {'widget': AdminRedactorEditor(redactor_settings={'lang': 'de'})},
    }
    inlines = [CommentInline]
    list_display = ['title', 'author', 'created', 'published', ]
    list_filter = ['created', 'published']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']

    def save_form(self, request, form, change):
        obj = super(PostAdmin, self).save_form(request, form, change)
        if not change:
            obj.author = request.user
        return obj


class CommentAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'author', 'created', 'post', 'published']
    list_filter = ['post']
    search_fields = ['author', 'body']


class PageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminRedactorEditor(redactor_settings={'lang': 'de'})},
    }
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'rank']
    search_fields = ['title', 'body']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_header = 'Administration'