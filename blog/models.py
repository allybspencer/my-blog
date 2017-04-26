from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title