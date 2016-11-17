from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index.as_view(),name='index'),
    url(r'^insert/',views.Insert.as_view(),name='insert'),
    url(r'^details/(?P<pk>[a-zA-Z0-9]+)/$',views.result.as_view(),name='details'),
    url(r'^details/$',views.result.as_view(),name='result'),
    
]