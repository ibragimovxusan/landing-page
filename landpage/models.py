from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CatchUser(AbstractUser):
    # Your custom fields and methods here

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    
    enter_the_vebinar = models.BooleanField(default=False)
    # Add unique related_name for groups
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='catchuser_set'  # Change 'catchuser_set' to any unique related name you prefer
    )

    # Add unique related_name for user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='catchuser_set'  # Change 'catchuser_set' to any unique related name you prefer
    )



class Deadline(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.datetime.date()} {self.datetime.time()}"