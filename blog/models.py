from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
        
class HitCount(models.Model):
    hits = models.IntegerField()
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    #comment_day = models.DateTimeField('date posted', blank=True, null=True)
    
    def __str__(self):
        return self.text
    