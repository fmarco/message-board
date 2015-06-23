from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    author = models.ForeignKey(User)
    message = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)

    def __unicode__(self):
        return  "Message %s" % self.pk
