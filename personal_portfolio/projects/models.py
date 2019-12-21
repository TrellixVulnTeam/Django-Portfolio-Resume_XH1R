from django.db import models
from django.urls import reverse
from PIL import Image


# Create your models here.
class Project(models.Model):
    slug = models.SlugField(null=False, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    github = models.CharField(max_length=100, null=True)
    #image = models.FilePathField(path="/img", null=True, blank=True)
    image = models.ImageField(default='default.png', upload_to="personal_portfolio//static//img", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def __str__(self):

        return self.title