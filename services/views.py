from __future__ import unicode_literals
from django.core.urlresolvers import resolve
from django.shortcuts import render,render_to_response

def openServicesDecoPage(request):
    current_url = resolve(request.path_info).url_name
    print  current_url
    return render_to_response('services/deco/decorationThemes.html', {})

def openServicesCateringPage(request):
    current_url = resolve(request.path_info).url_name
    print  current_url
    return render_to_response('services/catering/cateringAndMenu.html', {})

def openServicesLightPage(request):
    current_url = resolve(request.path_info).url_name
    print  current_url
    return render_to_response('services/light/lightAndSound.html', {})