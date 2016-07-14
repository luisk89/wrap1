from django.core.mail.message import EmailMultiAlternatives
from django.core.urlresolvers import reverse_lazy
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, DeleteView
from content.models import contact, slider, Service, Inbox, news
from multimedia.models import partner
from wrap.forms import formulario, form_news
from django.contrib import messages


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['contacto'] = contact.objects.first()
        context['slider'] = slider.objects.first()
        context['services'] = Service.objects.all()
        context['partners'] = partner.objects.all()
        return context

    # def enviar_form_ajax(request):
    #     if request.is_ajax():
    #         email = request.POST['email']
    #         form = news(email=email)
    #         msg = EmailMultiAlternatives(subject='Newsletter-new inscription',
    #                                      from_email=email,
    #                                      to=['bigbosss89@gmail.com'])
    #         html_content = '<h1>Newsletter-new inscription</h1><h5>Mail: %s</h5>' % (email)
    #         msg.attach_alternative(html_content, "text/html")
    #         msg_client = EmailMultiAlternatives(subject='Its a wrap and Printing - Newsletter',
    #                                             from_email='bigbosss89@gmail.com',
    #                                             to=[email])
    #         html_content = '<h1>Its a wrap and Printing - Newsletter</h1><h5>You have been registered in the Its a wrap and printing news service</h5><small>If you no longer wish to receive email from us, you can <a href="127.0.0.1:8000/del-news/%s">click here</a> to be inmediately unsubscribed</small>'% (email)
    #         msg.attach_alternative(html_content, "text/html")
    #         form.save()
    #
    #         msg.send()
    #         response = JsonResponse({'message': 'Your email has been sent.'})
    #         return HttpResponse(response.content)
    #
    #     else:
    #         return redirect('/')
    #
    # def del_news(request,email):
    #     news.objects.filter(email=email).update(is_active=False)
    #
    #     return redirect('/see-you/')

class Contact(FormView):
    template_name = 'contact.html'
    form_class = formulario
    success_url = reverse_lazy('contactform')

    def form_valid(self, form):
        form.save()
        form.send_email()
        messages.success(self.request, 'Your email has been sent.')
        return super(Contact, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Contact, self).get_context_data(**kwargs)
        context['contacto'] = contact.objects.first()
        context['slider'] = slider.objects.first()
        context['partners'] = partner.objects.all()
        return context


class Newsletter(FormView):
    template_name = 'index.html'
    form_class = formulario
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        form.send_email()
        messages.success(self.request, 'Your email has been sent.')
        return super(Newsletter, self).form_valid(form)


class unsuscribe(TemplateView):
    template_name = 'unsuscribe.html'

    def get_context_data(self, **kwargs):
        context = super(unsuscribe, self).get_context_data(**kwargs)
        context['contacto'] = contact.objects.first()
        return context