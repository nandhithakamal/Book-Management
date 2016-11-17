from django.core.urlresolvers import reverse
from django.db import models

class book(models.Model):
    title=models.CharField(max_length=100,primary_key=True)
    author = models.CharField(max_length=100)
    edition = models.IntegerField(default=1)
    totalpages = models.IntegerField(default=0)
    def get_absolute_url(self):
        return reverse('details', kwargs= {'pk' : self.title})
    def __str__(self):
        return self.title + '-' + self.author + '-' + self.edition + '-' + self.totalpages