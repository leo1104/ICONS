from django.db import models

# Create your models here.

class ContactUs(models.Model):
    """Model definition for contactus."""
    email=models.EmailField(max_length = 254)
    message=models.TextField()
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.email


class News(models.Model):
    title =  models.CharField(max_length=200)
    desc =  models.TextField()
    news_link =  models.URLField(max_length=200)

    def __str__(self):
        return self.title