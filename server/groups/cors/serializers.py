from rest_framework import serializers
from .models import Tag, Group, Image, Alert


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class GroupSerializer(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'link', 'description', 'tag', 'tag_name']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'url', 'group']


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'description', 'group']
