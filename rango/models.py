from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    NAME_MAX_LEN = 128

    name = models.CharField(max_length=NAME_MAX_LEN, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Page(models.Model):
    PAGE_MAX_LEN = 128
    URL_MAX_LEN = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=PAGE_MAX_LEN)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title