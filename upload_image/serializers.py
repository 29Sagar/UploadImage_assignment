from .models import *
from rest_framework import serializers
from django.core.exceptions import ValidationError
from drf_extra_fields.fields import Base64ImageField


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadImage
        fields = ('image', )

