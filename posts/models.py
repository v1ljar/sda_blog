from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.utils import timezone
=======
from django.urls import reverse
>>>>>>> origin/ClassBasedViews

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    updated_at = models.DateTimeField(default=timezone.now)
=======
    updated_at = models.DateTimeField(auto_now=True)
>>>>>>> origin/ClassBasedViews
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
