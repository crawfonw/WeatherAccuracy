from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = models.TextField()
    post_date = models.DateTimeField()
    is_draft = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('-post_date',)
    
    def __unicode__(self):
        return unicode(self.title)