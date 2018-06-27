from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)    
    title = models.CharField(max_length=200)
    url = models.URLField(default='Your Website')    
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
