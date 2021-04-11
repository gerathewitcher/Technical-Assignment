from rest_framework import viewsets
from .models import News
from .serlializers import NewsSerializer

class NewsAPIView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer