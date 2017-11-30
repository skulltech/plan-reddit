from django.db import models
from django.core.exceptions import ValidationError


class Post(models.Model):
    subreddit = models.CharField(max_length=20)
    title = models.CharField(max_length=256)
    text = models.TextField(max_length=40000)
    link = models.URLField()
    time = models.DateTimeField()

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        link = cleaned_data.get('link')

        if text and link:
            raise ValidationError('You can provide only one of text and link, not both!')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
