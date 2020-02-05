from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')    


