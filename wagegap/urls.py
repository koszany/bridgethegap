from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.contact_view, name='your-wage')
    #url(r'^search-form/$', views.search_form),
]
