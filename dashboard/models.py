
# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "dashboard_post"
