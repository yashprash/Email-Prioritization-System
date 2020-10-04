from django.db import models

# Create your models here.


class Email(models.Model):
    from_mail = models.EmailField()
    to_mail = models.EmailField()
    from_name = models.CharField(max_length=25)
    to_name = models.CharField(max_length=25)
    subject = models.CharField(max_length=256)
    body = models.TextField()
    date = models.DateTimeField()
    priority = models.CharField(max_length=256)

