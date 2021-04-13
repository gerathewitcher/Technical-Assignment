from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from .tasks import create_news


class NewsAPIView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


