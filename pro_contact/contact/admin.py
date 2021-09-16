from django.contrib import admin
from django.contrib import admin
from .models import Phonebook
# Register your models here.
admin.site.register(Phonebook)
class PhonebookAdmin(admin.ModelAdmin):
    list_display =('id','name','Phone_num')
