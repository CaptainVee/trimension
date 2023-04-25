from django.db import models
from django.conf import settings

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ["created_at"]

class Book(BaseModel):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=True, blank=True)


class Page(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False, null=False)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    model = models.FileField(null=True, blank=True, upload_to ='uploads/')

    site_name = models.CharField(max_length=500, blank=False, null=False)
    site_id = models.CharField(max_length=500, blank=False, null=False)
    site_url = models.URLField(null=True, blank=True)
