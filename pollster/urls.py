"""pollster URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

# FARI got error while following tutorial which was for django 2.*; i'm using 1.*
# from django.urls import include, path
# this worked
from django.conf.urls import include

urlpatterns = [
    # FARI got error due to django version
    #path('pools/', include('poll.url')),

    # also I have to put the '' at the bottom to avoid catching all as well as any non-specific ones .... not sure what's the better way of doing this

    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    url(r'^', include('pages.urls')),
]
