from django.db import models

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(
        User, through="TeamMembership", related_name="members"
    )
    description = models.TextField()


class Role(models.Model):
    name = models.CharField(max_length=64)


class TeamMembership(models.Model):
    user = models.ForeignKey(
        User, related_name="membership", on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        Team, related_name="membership", on_delete=models.CASCADE
    )
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    involvement = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )


class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    teams = models.ManyToManyField(Team, related_name="teams")
    client = models.ForeignKey(
        "clients.Client", null=True, on_delete=models.CASCADE
    )
    is_global = models.BooleanField(default=False)
    is_internal = models.BooleanField(default=False)

    # TODO: Rethink later permissions
    # class Meta:
    #     permissions = [
    #         ("can_edit_project", "Can edit project"),
    #     ]

