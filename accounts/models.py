from django.db import models


class Account(models.Model):
    owner = models.CharField(max_length=100)
    balance = models.FloatField(default=0.0)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('owner',)

    def __str__(self):
        return self.owner
