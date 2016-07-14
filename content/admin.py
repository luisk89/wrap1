from django.contrib import admin

# Register your models here.
from content import models

admin.site.register(models.slider)
admin.site.register(models.contact)
admin.site.register(models.Inbox)
admin.site.register(models.Service)
admin.site.register(models.item)
admin.site.register(models.pricing)
admin.site.register(models.ServiceContent)
admin.site.register(models.news)
