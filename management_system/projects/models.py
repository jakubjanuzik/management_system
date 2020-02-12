from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(
        User, through="TeamMembership", related_name="teams"
    )
    description = models.TextField()

    def __str__(self):
        return f"Team - {self.name}"


class Role(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"Role - {self.name}"


class TeamMembership(models.Model):
    user = models.ForeignKey(
        User, related_name="membership", on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        Team, related_name="membership", on_delete=models.CASCADE
    )
    role = models.ManyToManyField(Role, blank=True)
    involvement = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )


class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    teams = models.ManyToManyField(Team, related_name="teams")
    client = models.ForeignKey(
        "clients.Client", null=True, on_delete=models.CASCADE, blank=True
    )
    is_global = models.BooleanField(default=False)
    is_internal = models.BooleanField(default=False)

    # TODO: Rethink later permissions
    # class Meta:
    #     permissions = [
    #         ("can_edit_project", "Can edit project"),
    #     ]

    def __str__(self):
        return f"Project - {self.name}"
