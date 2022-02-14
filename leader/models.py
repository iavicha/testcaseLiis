from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Leader(models.Model):
    name = models.CharField(max_length=30, default="No name")
    text = models.TextField(max_length=2400)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=User, null=True, blank=True, editable=True)

    LEADER_STATUS = (
        ('P', 'Public'),
        ('S', 'Subscription'),
    )
    leader_status = models.CharField(max_length=1, choices=LEADER_STATUS)

    def __str__(self):
        return self.name
