from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('purchase-power', views.purchase_power, name='purchase-power')
    #url(r'^search-form/$', views.search_form),
]
