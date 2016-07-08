from django.db import models
from django.core.urlresolvers import reverse
from content.models import Service


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


# Create your models here.
class categoria(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name

class gallery(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = 'gallery/photo',null=True,blank=True)
    publish = models.BooleanField(default=True)
    categoria=models.ForeignKey(categoria,null=True,blank=True)
    video=models.FileField(upload_to='gallery/video',blank=True,null=True)

    objects = EntryQuerySet.as_manager()

    _metadata = {
        'title': 'name',
        'description': 'abstract',
    }


    def __unicode__(self):
        return self.title

class partner(models.Model):
    name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='photo/partners')

    def __str__(self):
        return self.name
