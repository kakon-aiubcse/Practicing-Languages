from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    titles = models.CharField(max_length=40)
    content = models.TextField()
    def __str__(self):  # Optional, for nicer admin display
        return self.titles
