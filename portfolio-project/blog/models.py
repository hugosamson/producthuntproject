from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, null=True)
    pub_date = models.DateTimeField(null=True)
    body = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to='images/')
