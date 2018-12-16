from django.db import models


# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=255, default='')
    stars = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
