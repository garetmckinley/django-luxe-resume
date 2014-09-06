from django.db import models
from django.core.urlresolvers import reverse


class Bio(models.Model):
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    #avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    about = models.TextField()

    def __unicode__(self):
        return u'%s' % self.name

#class Skill()
