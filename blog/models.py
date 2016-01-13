from django.db import models

# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 16)

    def __unicode__(self):
        return u'%s' % (self.username)

class Article(models.Model):
    title = models.CharField(max_length = 100)
    publishtime = models.DateTimeField(auto_now_add = True)
    usernameid = models.CharField(max_length = 20)
    author = models.CharField(max_length = 50)
    body = models.TextField()

    def __unicode__(self):
        return u'%s' % (self.title)

    class Meta:
        ordering = ['-publishtime']