"""baraati URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from homepage import views as homepageViews
from gallery import views as galleryViews
from aboutUs import views as aboutUsViews
from blog import views as blogViews
from booking import views as bookingViews
from contact import views as contactViews
from faqs import views as faqsViews
from services import views as serviceViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',homepageViews.openHomePage,name='open_homepage'),
    url(r'^gallery/',galleryViews.openGalleryPage,name='open_gallery'),
    url(r'^about/', aboutUsViews.openAboutUsPage, name='open_about'),
    url(r'^blog/', blogViews.openBlogPage, name='open_blog'),
    url(r'^booking/', bookingViews.openBookingPage, name='open_booking'),
    url(r'^contact/', contactViews.openContactPage, name='open_contact'),
    url(r'^faqs/', faqsViews.openFaqsPage, name='open_faqs'),
    url(r'^services/deco/', serviceViews.openServicesDecoPage, name='open_services_deco'),
    url(r'^services/catering/', serviceViews.openServicesCateringPage, name='open_services_catering'),
    url(r'^services/light/', serviceViews.openServicesLightPage, name='open_services_light'),
]

