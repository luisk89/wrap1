"""wrap_printing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.views.generic.base import TemplateView
from content import views
from multimedia.views import Gallery
from wrap.views import Index, Contact
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^$',Index.as_view(), name="home"),

    url(r'^gallery/',Gallery.as_view(), name="gallery"),
    #url(r'^enviarform/',Index.enviar_form_ajax, name="contact"),

    url(r'^contact/',Contact.as_view(), name="contactform"),

    url(r'^service/(?P<pk>\S+)$', views.ServicesDetail.as_view(), name="service-single"),
    url(r'^services/', views.Services.as_view(), name="services"),
]

if getattr(settings, "DEBUG", False):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
