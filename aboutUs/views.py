# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import resolve
from django.shortcuts import render,render_to_response

def openAboutUsPage(request):
    current_url = resolve(request.path_info).url_name
    print  current_url
    return render_to_response('aboutUs/aboutUs.html', {})