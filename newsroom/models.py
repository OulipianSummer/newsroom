from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify 

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(null=True, unique=True)
    section = models.ForeignKey(to="Section", related_name='article_section', on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to="Author", related_name='article_author', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Section(models.Model):
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Author(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    title = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True, max_length=300)
    picture = models.URLField(blank=True)
  

    def __str__(self):
        return f"{self.first} {self.last}"
