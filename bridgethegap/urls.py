"""bridgethegap URL Configuration

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
from django.urls import include, path

urlpatterns = [
<<<<<<< HEAD
    path('wagegap/', include('wagegap.urls')),
    path('your-wage/', include('wagegap.urls')),
=======
    path('wage/', include('wage.urls')),
    path('your-wage/', include('wage.urls')),
>>>>>>> 7302cf3a0a02a6d88ca437dd83c82703a7887c47
    url(r'^admin/', admin.site.urls),
]
