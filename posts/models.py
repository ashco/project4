from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField( default=datetime.now, blank = True )
    def __str__(self):
        return self.title #show title in admin page
    # class Meta:
    #     verbose_name_plural = 'Posts' #makes posts database singular