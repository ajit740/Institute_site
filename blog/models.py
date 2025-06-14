from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    published_date = models.DateField()
    summary = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
