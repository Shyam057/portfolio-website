from django.db import models

class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)  # e.g. "Backend Developer"
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "About"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('languages', 'Languages'),
        ('web', 'Web & Backend'),
        ('database', 'Databases'),
        ('tools', 'Tools'),
        ('concepts', 'CS Concepts'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        ordering = ['order']


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=20)  # or "Expected 2027"
    gpa = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        ordering = ['order']


class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)  # or "Present"
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.job_title} at {self.company}"

    class Meta:
        ordering = ['order']