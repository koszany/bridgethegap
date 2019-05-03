from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #url(r'^search-form/$', views.search_form),
]
