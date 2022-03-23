from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=20)
    duration = models.IntegerField()
    last_play = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
