from rest_framework import serializers
from .models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField()  # Add this line

    class Meta:
        model = User
        fields = ['user_id', 'role', 'role_name', 'banned']  # Add 'role_name' here

    def get_role_name(self, obj):
        return obj.role.name
