from rest_framework import viewsets
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from .models import Tag, Group, Image, Alert
from .serializers import TagSerializer, GroupSerializer, ImageSerializer, AlertSerializer


class GroupViewSet(viewsets.ViewSet):
    def list(self, request):
        group_id = request.data.get('group_id')
        groups = Group.objects.filter(is_active=True, filter=group_id)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def create(self, request):
        images = request.data["images"]
        del request.data["images"]
        serializer = GroupSerializer(data=request.data)
        for image in images:
            imageSerializer = ImageSerializer(image=image)
            if imageSerializer.is_valid():
                serializer.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request):
        try:
            link = request.data['link']
            group = Image.objects.get(link=link)
            images = Image.objects.filter(group=group["id"])
            for image in images:
                image.delete()
            group.delete()
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"message": "Group not found"}, status=404)
        except ValidationError:
            return Response({"message": "Invalid ID"}, status=400)

    def update(self, request, pk=None):
        try:
            link = request.data['link']
            group = Group.objects.get(link=link)
            serializer = GroupSerializer(group, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except ObjectDoesNotExist:
            return Response({"message": "Group not found"}, status=404)
        except ValidationError:
            return Response({"message": "Invalid data"}, status=400)


class ImageViewSet(viewsets.ViewSet):
    def list(self, request):
        group_id = request.data.get('group_id')
        images = Image.objects.filter(group=group_id)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            image = Image.objects.get(id=pk)
            image.delete()
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"message": "Image not found"}, status=404)
        except ValidationError:
            return Response({"message": "Invalid ID"}, status=400)


class AlertViewSet(viewsets.ViewSet):
    def list(self, request):
        group_id = request.data.get('group_id')
        alerts = Alert.objects.filter(group=group_id)
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request):
        try:
            link = request.data['link']
            alert = Alert.objects.get(link=link)
            alert.delete()
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"message": "Alert not found"}, status=404)
        except ValidationError:
            return Response({"message": "Invalid ID"}, status=400)


class TagViewSet(viewsets.ViewSet):
    def list(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            image = Tag.objects.get(id=pk)
            image.delete()
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"message": "Image not found"}, status=404)
        except ValidationError:
            return Response({"message": "Invalid ID"}, status=400)

    def update(self, request, pk=None):
        try:
            tag = Tag.objects.get(id=pk)
            serializer = TagSerializer(tag, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except ObjectDoesNotExist:
            return Response({"message": "Image not found"}, status=404)
        except ValidationError:
            return Response({"message": "Invalid data"}, status=400)
