from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='your-wage')
    #url(r'^search-form/$', views.search_form),
]
