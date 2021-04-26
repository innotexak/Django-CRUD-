from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static')
    body = models.TextField()
    author = models.CharField(max_length=15)
    timstamp = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return f"{self.title}"
