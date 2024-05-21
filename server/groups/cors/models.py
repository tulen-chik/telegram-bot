from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Group(models.Model):
    link = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Image(models.Model):
    url = models.ImageField(upload_to='images/')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Alert(models.Model):
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
