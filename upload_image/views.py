from django.shortcuts import HttpResponse, render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from upload_image.models import UploadImage
from .serializers import ImageSerializer

# Create your views here.
class ImageViewSet(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthenticated]
    queryset = UploadImage.objects.all()
    serializer_class = ImageSerializer