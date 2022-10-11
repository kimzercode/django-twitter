from django.db import models

class Tweet(models.Model):
    message = models.CharField(max_length=50)
    name = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message