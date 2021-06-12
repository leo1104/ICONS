from django.contrib import admin
from home.models import ContactUs, News

#!dont forget this and even importing the contactus 
# Register your models here.
admin.site.register(ContactUs)
admin.site.register(News)
