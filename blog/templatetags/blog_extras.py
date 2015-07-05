#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Julia Wallmüller'

from django import template

register = template.Library()


# a custom template filter
# (die calender.month_name methode liefert leider nur die en version
def month_name(month_number):
    return {
        1: 'Januar',
        2: 'Februar',
        3: 'März',
        4: 'April',
        5: 'Mai',
        6: 'Juni',
        7: 'Juli',
        8: 'August',
        9: 'September',
        10: 'Oktober',
        11: 'November',
        12: 'Dezember',
    }.get(month_number)

register.filter('month_name', month_name)