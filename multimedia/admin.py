from django.contrib import admin

# Register your models here.
from multimedia import models

admin.site.register(models.gallery)
admin.site.register(models.categoria)
admin.site.register(models.partner)

