from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from .models import Role, User
from .serializers import RoleSerializer, UserSerializer

import json


class RoleViewSet(viewsets.ViewSet):
    def list(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request):
        try:
            role = Role.objects.get(id=request.data['role_id'])
            role.delete()
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"message": "Role not found"}, status=404)
        except ValidationError:
            return Response({"message": "Invalid ID"}, status=400)

    def update(self, request,):
        try:
            role = Role.objects.get(id=request.data['role_id'])
            serializer = RoleSerializer(role, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except ObjectDoesNotExist:
            return Response({"message": "Role not found"}, status=404)
        except ValidationError:
            return Response({"message": "Invalid data"}, status=400)


class UserViewSet(viewsets.ViewSet):
    def retrieve(self, request):
        try:
            user = User.objects.get(user_id=request.data['user_id'])
            role_name = user.role.name  # Accessing the related Role object
            serializer = UserSerializer(user)
            data = serializer.data
            data['role_name'] = role_name  # Adding role name to the response
            return Response(data)
        except ObjectDoesNotExist:
            return Response({"message": "User not found"}, status=404)
        except ValidationError:
            return Response({"message": "Invalid link"}, status=400)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request):
        try:
            user = User.objects.get(id=request.data["user_id"])
            user.delete()
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"message": "User not found"}, status=404)
        except ValidationError:
            return Response({"message": "Invalid ID"}, status=400)

    def update(self, request):
        try:
            user = User.objects.get(id=request.data["user_id"])
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except ObjectDoesNotExist:
            return Response({"message": "User not found"}, status=404)
        except ValidationError:
            return Response({"message": "Invalid data"}, status=400)
