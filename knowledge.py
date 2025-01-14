from django.db import models
from django.utils.timezone import now

class Knowledge(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ('recycling', 'Recycling'),
        ('energy', 'Renewable Energy'),
        ('water', 'Water Conservation'),
        ('climate', 'Climate Change'),
    ])
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.category})"

    def get_snippet(self, length=100):
        """
        Returns a snippet of the content with a specified length.
        """
        return f"{self.content[:length]}..." if len(self.content) > length else self.content
