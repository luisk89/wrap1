from django.db import models

# Create your models here.
# coding=utf-8
from django.db import models


# Create your models here.
from django.utils.timezone import now


class slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Photo/slider', blank=False)

    def __unicode__(self):
        return self.title


class contact(models.Model):
    logo = models.ImageField(upload_to='Photo/logo', blank=False)
    phone_number = models.CharField(blank=True, max_length=15)
    mail_contact = models.EmailField(max_length=70, blank=True)
    fax = models.CharField(blank=True, max_length=20)
    address = models.CharField(max_length=200)
    information = models.CharField(max_length=500)
    website = models.CharField(max_length=100)
    facebook = models.CharField(max_length=150, blank=True)
    twitter = models.CharField(max_length=150, blank=True)
    google = models.CharField(max_length=150, blank=True)
    instgram = models.CharField(max_length=150, blank=True)
    skype = models.CharField(max_length=150, blank=True)
    bannertop=models.ImageField(upload_to='Photo/banner',blank=True,null=True)

    def __unicode__(self):
        return self.address


class Inbox(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, null=True, blank=True)
    mail_contact = models.EmailField(max_length=70, blank=True)
    phone_number = models.CharField(blank=True, max_length=15)
    message = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Service(models.Model):
    tipo = models.CharField(blank=True, max_length=15)
    name = models.CharField(max_length=250)
    resumen = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    bannertop=models.ImageField(upload_to='Photo/banner',null=True,blank=True)
    icon=models.CharField(max_length=250,blank=True,null=True)
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ServiceContent(models.Model):
    name = models.CharField(max_length=200)
    texto = models.TextField(blank=True)
    foto_portada = models.ImageField(upload_to='Photo/service', blank=False)
    service = models.ForeignKey(Service)


class item(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='Photo/item', blank=False)
    service = models.ForeignKey(Service)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(
        default=False)
        # solo debe haber un solo item activo por cada servicio para q no entre en conflicto con el listitem del index

    def __unicode__(self):
        return self.name


class pricing(models.Model):
    service = models.ForeignKey(Service)
    name = models.CharField(max_length=20)
    precio_min = models.IntegerField()
    precio_max = models.IntegerField()

class news(models.Model):
    email = models.EmailField(max_length=70,unique=True)
    alta_date_created=models.DateField(auto_now_add=now())
    baja_date_created = models.DateField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
