from django.db import models
from slugify import slugify

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    about = models.TextField()
    image = models.ImageField(upload_to='author_images')
    slug = models.SlugField(primary_key=True, blank=True,max_length=120)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name) + '_' + slugify(self.last_name)
        return super().save(*args, **kwargs)

    def __str__(self) :
        return f'{self.last_name} {self.last_name}'
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        