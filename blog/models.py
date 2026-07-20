from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    excerpt = models.TextField(help_text="Short summary shown on the news list card.")
    body = models.TextField(blank=True, help_text="Full article content shown on the post detail page.")
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    published_at = models.DateTimeField()
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})
