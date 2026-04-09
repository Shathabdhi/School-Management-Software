from rest_framework import viewsets

from .models import Notice
from .serializers import NoticeSerializer


# Create your views here.
class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
