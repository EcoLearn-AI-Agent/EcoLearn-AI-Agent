from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=200)
    description = models.TextField()
    points_reward = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def mark_as_completed(self):
        """
        Marks the task as completed and updates the completion timestamp.
        """
        self.is_completed = True
        self.completed_at = models.DateTimeField(auto_now=True)
        self.user.add_points(self.points_reward)  # Award points to the user
        self.save()

    def __str__(self):
        return f"Task: {self.title} (Points: {self.points_reward})"
