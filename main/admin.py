from django.contrib import admin

# Register your models here.
from models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ('id','Lurl','Surl')
    search_fields = ('id','Lurl','Surl')

admin.site.register(Url, UrlAdmin)
