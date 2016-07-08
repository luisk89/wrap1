from django.core.mail.message import EmailMultiAlternatives
from django.core.urlresolvers import reverse_lazy
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from content.models import contact, slider, Service, Inbox
from multimedia.models import partner
from wrap.forms import formulario
from django.contrib import messages

class Index (TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['contacto'] = contact.objects.first()
        context['slider'] = slider.objects.first()
        context['services']=Service.objects.all()
        context['partners']=partner.objects.all()
        return context

    def enviar_form_ajax(request):
        if request.is_ajax():
            name=request.POST['name']
            phone=request.POST['phone']
            mail=request.POST['mail']
            subject=request.POST['subject']
            message=request.POST['message']
            form=Inbox(name=name,phone_number=phone,mail_contact=mail,subject=subject,message=message)
            msg= EmailMultiAlternatives(subject= subject,
                        from_email = mail,
                        to=['bigbosss89@gmail.com'])
            html_content = '<h5>Name: %s</h5><h5>Mail: %s</h5><h5>Phone: %s</h5><h5>Message: %s</h5>' % (name,mail,phone,message)
            msg.attach_alternative(html_content, "text/html")
            #msg.send()
            form.save()
            response=JsonResponse({'message':'Mensaje enviado'})
            return HttpResponse(response.content)
        else:
            return redirect('/')

class Contact (FormView):
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
        context['partners']=partner.objects.all()
        return context
