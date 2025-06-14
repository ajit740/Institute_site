from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='events/images/', blank=True, null=True)

    def __str__(self):
        return self.title
