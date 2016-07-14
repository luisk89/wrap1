from django import forms
from django.core.mail.message import EmailMultiAlternatives
from content.models import Inbox, news

__author__ = 'Luisk'

class formulario(forms.Form):
    class Meta:
        model=Inbox

    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name','size':'30','type':'text','required':'required','class':'form-control placeholder'}),required=True)
    mail = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email','type':'email','size':'30','required':'required','class':'form-control placeholder'}),required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone','type':'text','size':'30','required':'required','class':'form-control placeholder'}),required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Comments','type':'text','size':'30','required':'required','rows':'7','class':'form-control placeholder'}), required=True)
    subject=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject','size':'30','type':'text','required':'required','class':'form-control placeholder'}),required=True)
    def send_email(self):
        name=self.cleaned_data['name']
        mail=self.cleaned_data['mail']
        phone=self.cleaned_data['phone']
        message=self.cleaned_data['message']
        subject=self.cleaned_data['subject']
        msg= EmailMultiAlternatives(subject= subject,
                        from_email = mail,
                        to=['bigbosss89@gmail.com'])
        html_content = '<h5>Name: %s</h5><h5>Mail: %s</h5><h5>Phone: %s</h5><h5>Message: %s</h5>' % (name,mail,phone,message)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def save(self):
        data = self.cleaned_data
        reserva=Inbox(name=data['name'], mail_contact=data['mail'], phone_number=data['phone'], message=data['message'],subject=data['subject'])
        reserva.save()

class form_news(forms.Form):
    class Meta:
        model=news

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email','type':'email','size':'30','required':'required','class':'form-control placeholder'}),required=True)

    def send_email(self):
        email=self.cleaned_data['mail']
        msg= EmailMultiAlternatives(subject= 'Newsletter-new inscription',
                        from_email = email,
                        to=['bigbosss89@gmail.com'])
        html_content = '<h5>Mail: %s</h5>' % (email)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def save(self):
        data = self.cleaned_data
        noticias=news(email=data['email'])
        noticias.save()
