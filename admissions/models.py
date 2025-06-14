from django.db import models

# Create your models here.
# admissions/models.py
from django.db import models

class Application(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    applied_course = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"{self.full_name} - {self.applied_course}"


class Document(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="documents")
    doc_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return f"{self.doc_name} for {self.application.full_name}"
