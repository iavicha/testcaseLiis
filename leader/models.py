from django.db import models
from django.conf import settings


# Create your models here.

class Leader(models.Model):
    name = models.CharField(max_length=30, default="No name")
    text = models.TextField(max_length=2400)
    user = settings.AUTH_USER_MODEL

    author = models.ForeignKey(user, on_delete=models.CASCADE, default=user)

    LEADER_STATUS = (
        ('P', 'Public'),
        ('S', 'Subscription'),
        ('A', 'Archive'),
    )
    leader_status = models.CharField(max_length=1, choices=LEADER_STATUS)

    def __str__(self):
        return self.name
