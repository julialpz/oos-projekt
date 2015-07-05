#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Julia Wallmüller'

import hashlib

from collections import OrderedDict
from django.core.context_processors import csrf
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from models import *

brand = 'Toller Name'
pages = Page.objects.all


# returns a dictionary with standard arguments used in all views
def get_dictionary(request):
    d = {}
    d.update(csrf(request))
    d.update({'brand': brand, 'pages': pages, 'user': request.user})
    return d


# returns query object with all currently published posts
def get_published_posts():
    return Post.objects.filter(published=True)


# returns an ordered dictionary with all currently published posts in descending order
# schema: {'year': {'month': [posts]}}
def mk_archive_list():
    posts = get_published_posts()
    archive_list = OrderedDict()

    for p in posts:
        year = p.created.year
        month = p.created.month

        if year not in archive_list:
            archive_list.update({year: {}})

        if month not in archive_list[year]:
            archive_list[year].update({month: []})

        archive_list[year][month].append(p)

    return archive_list


# returns a list of all currently populated categories
def mk_cat_list():
    cat_query = Category.objects.all()
    cat_list = []

    for c in cat_query:
        if len(get_published_posts().filter(categories=c)) > 0:
            cat_list.append(c)

    return cat_list


# returns current users real name (if given) or user name
def get_name(request):
    if request.user.first_name and request.user.last_name:
        return '%s %s' % (request.user.first_name, request.user.last_name, )
    else:
        return request.user.username


# renders a list view of all currently published posts with pagination (if necessary)
def index(request, posts=None):
    if posts is None:
        posts = get_published_posts()

    paginator = Paginator(posts, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    d = get_dictionary(request)
    d.update({'title': 'Blog', 'posts': posts})

    return render(request, 'blog/index.html', d)


# renders detail view of a single post, with comments, comment form and sidebar widgets
def post(request, year, month, day, slug):
    post = get_object_or_404(get_published_posts().filter(slug=slug)
                             .filter(created__year=year, created__month=month, created__day=day))

    # this handles the POST request from the comment form and/or creates the comment form
    if request.method == 'POST':
        if request.user.is_authenticated():
            cf = UserCommentForm(request.POST)
        else:
            cf = CommentForm(request.POST)
        r = request.POST
        if cf.is_valid():
            comment = Comment(post=post)
            if request.user.is_authenticated():
                comment.author = get_name(request)
                comment.email = request.user.email
            else:
                comment.author = r['author']
                comment.email = r['email']
            comment.body = r['body']
            comment.gravatar_hash = hashlib.md5(comment.email.strip().lower()).hexdigest()
            if r['url']:
                comment.url = r['url']
            comment.save()
            return HttpResponseRedirect('')
    else:
        if request.user.is_authenticated():
            cf = UserCommentForm()
        else:
            cf = CommentForm()

    comments = Comment.objects.filter(post=post)

    d = get_dictionary(request)
    d.update({'post': post, 'cf': cf, 'comments': comments, 'archive_list': mk_archive_list(),
              'categories': mk_cat_list()})

    return render(request, 'blog/post.html', d)


# filters currently published posts for year and sends them to index view
def year(request, year):
    posts = get_published_posts().filter(created__year=year)
    return index(request, posts)


# filters currently published posts for year and month and sends them to index view
def month(request, year, month):
    posts = get_published_posts().filter(created__year=year).filter(created__month=month)
    return index(request, posts)


# filters currently published posts for category and sends them to index view
def category(request, slug):
    posts = get_published_posts().filter(categories__slug=slug)
    return index(request, posts)


# renders single page view of specified page
def page(request, slug):
    page = get_object_or_404(Page.objects.filter(slug=slug))
    d = get_dictionary(request)
    d.update({'page': page})

    if slug == 'archiv':

        # this renders the archive view with an archive list (see mk_archive_list)
        template = 'blog/archive.html'
        d.update({'archive_list': mk_archive_list()})

    elif slug == 'kontakt':

        # this handles the POST request from the contact form and/or creates the contact form
        if request.method == 'POST':
            cf = ContactForm(request.POST)
            r = request.POST
            if cf.is_valid():
                subject = '%s: Kontaktformular' % brand
                message = '%s (%s): %s' % (r['name'], r['email'], r['message'],)

                try:
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.DEFAULT_TO_EMAIL],
                              fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                return HttpResponseRedirect(reverse('blog:confirm', args=['danke']))
        else:
            init = {}

            if request.user.is_authenticated():
                init.update({'name': get_name(request), 'email': request.user.email})

            cf = ContactForm(initial=init)

        d.update({'cf': cf})
        template = 'blog/contact.html'

    else:
        template = 'blog/page.html'

    return render(request, template, d)


# this handles the POST request from the search form and renders the results page
def search(request):
    if request.method == "POST":
        query = request.POST['query']
    else:
        query = ''

    posts = get_published_posts().filter(Q(title__contains=query) | Q(body__contains=query))

    d = get_dictionary(request)
    d.update({'posts': posts, 'title': 'Suchergebnisse', 'query': query})

    return render(request, 'blog/search.html', d)