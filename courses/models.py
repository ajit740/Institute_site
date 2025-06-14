from django.db import models

PROGRAM_TYPES = [
    ('UG', 'Undergraduate'),
    ('PG', 'Postgraduate'),
    ('Diploma', 'Diploma'),
    ('Certification', 'Certification'),
]

class Course(models.Model):
    name = models.CharField(max_length=200)
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPES)
    # models.py
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    duration = models.CharField(max_length=100)
    syllabus = models.TextField()
    eligibility = models.TextField()

    def __str__(self):
        return self.name
from django.db import models

class Enrollment(models.Model):
    course_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_phone = models.CharField(max_length=15)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.course_name}"
