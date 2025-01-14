from django.db import models
from django.contrib.auth.models import User

class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rewards")
    points = models.IntegerField()
    reward_type = models.CharField(max_length=100, choices=[
        ('token', 'Eco Token'),
        ('discount', 'Eco Discount'),
        ('donation', 'Donation to Green Initiatives'),
    ])
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.reward_type} ({self.points} points)"
    
    def apply_reward(self):
        """
        Applies the reward to the user's account, such as adding tokens or discounts.
        This is a placeholder method and can be expanded based on the reward type.
        """
        if self.reward_type == 'token':
            self.user.add_points(self.points)  # Add eco tokens as points
        elif self.reward_type == 'discount':
            pass  # Add discount logic here
        elif self.reward_type == 'donation':
            pass  # Donation logic can be implemented here
        self.save()
