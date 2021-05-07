from django.db import models
from django.urls import reverse


class User(models.Model):

    username = models.CharField(max_length=50)
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})
