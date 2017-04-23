# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import resolve
from django.shortcuts import render,render_to_response


def openGalleryPage(request):
    current_url = resolve(request.path_info).url_name
    return render(request,'gallery/gallery.html', {})
