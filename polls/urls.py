#from django.urls import path

from django.conf.urls import url
from django.conf.urls import include

from . import views


app_name = 'polls'

urlpatterns = [
    # createing a route, need to bring it to the main urls.py in the outer directory
    #path('', view.index, name='index')

    #url('<int:question_id>/', views.detail, name='detail')
    # FARI above format using <int:question_id> only works in django 2.*
    # also I have to put the '' at the bottom to avoid catching all as well as any non-specific ones .... not sure what's the better way of doing this
    url('(?P<question_id>[0-9]+)/results', views.results, name='results'),
    url('(?P<question_id>[0-9]+)/vote', views.vote, name='vote'),
    url('(?P<question_id>[0-9]+)', views.detail, name='detail'),
    url('', views.index, name='index'),
]
