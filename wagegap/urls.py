from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('purchase-power/<country_name>&<wage>', views.purchase_power, name='purchase-power')
]
