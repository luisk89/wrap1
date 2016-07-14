from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from content.models import Service, contact, slider
from multimedia.models import partner


class ServicesDetail(DetailView):
    context_object_name = 'service'
    model = Service
    template_name = "service.html"

    def get_context_data(self, **kwargs):

        context = super(ServicesDetail, self).get_context_data(**kwargs)
        context['contacto'] = contact.objects.first()
        context['slider'] = slider.objects.first()
        # context['Items'] = Items
        return context

class Services(ListView):
    context_object_name = 'services'
    model = Service
    template_name = "services.html"

    def get_context_data(self, **kwargs):

        context = super(Services, self).get_context_data(**kwargs)
        context['contacto'] = contact.objects.first()
        context['slider'] = slider.objects.first()
        context['partners'] = partner.objects.all()
        return context



