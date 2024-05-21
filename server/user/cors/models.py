from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)


class User(models.Model):
    user_id = models.CharField(max_length=50, unique=True, primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=2)
    banned = models.BooleanField(default=False)
