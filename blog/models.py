#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Julia Wallmüller'

from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ModelForm
from django.utils import timezone

from crispy_forms.helper import FormHelper


# posts can be sorted into several categories
class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField('Permalink', unique=True)

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorien'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', args=[self.slug])


# single blog post
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField('Titel', max_length=60)
    slug = models.SlugField('Permalink', unique_for_date='created')
    created = models.DateTimeField('Erstellt am', default=timezone.now)
    body = models.TextField('Inhalt')
    image = models.ImageField('Beitragsbild', blank=True, upload_to='pictures/%Y/%m/%d')
    published = models.BooleanField('Veröffentlicht?', default=True)
    categories = models.ManyToManyField(Category, default=0)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Beitrag'
        verbose_name_plural = 'Beiträge'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.created.year, self.created.month, self.created.day, self.slug])

    # returns authors real name (if given) or username
    def get_author(self):
        if self.author.first_name and self.author.last_name:
            return '%s %s' % (self.author.first_name, self.author.last_name,)
        else:
            return self.author.username


# posts can have multiple comments
class Comment(models.Model):
    author = models.CharField('Name', max_length=60)
    email = models.EmailField('E-Mail')
    gravatar_hash = models.CharField(max_length=32, editable=False)
    url = models.URLField('Homepage', blank=True)
    body = models.TextField('Inhalt')
    created = models.DateTimeField('Erstellt am', auto_now_add=True)
    published = models.BooleanField('Veröffentlicht?', default=True)
    post = models.ForeignKey(Post)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Kommentar'
        verbose_name_plural = 'Kommentare'

    def __unicode__(self):
        return self.body[:60]


# comment form created from comment model
class CommentForm(ModelForm):

    class Meta:
        model = Comment
        exclude = ['post', 'published']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True


# this is used for authenticated users, author and email need to be filled with user info
class UserCommentForm(CommentForm):

    class Meta:
        model = Comment
        exclude = ['author', 'email', 'post', 'published']


# simple single page
class Page(models.Model):
    rank = models.SmallIntegerField('Rang', unique=True, blank=True, null=True,
                                    help_text='Bestimmt Reihenfolge im Hauptmenü, bei leerem Feld erscheint Seite nicht im Menü.')
    title = models.CharField('Titel', max_length=60)
    slug = models.SlugField('Permalink', unique=True)
    body = models.TextField('Inhalt', blank=True)

    class Meta:
        ordering = ['rank']
        verbose_name = 'Seite'
        verbose_name_plural = 'Seiten'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:page', args=[self.slug])


class ContactForm(forms.Form):
    name = forms.CharField(max_length=60)
    email = forms.EmailField(label='E-Mail')
    message = forms.CharField(label='Nachricht', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True