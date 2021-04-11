from django.urls import path
from rest_framework.routers import SimpleRouter

from .api_views import NewsAPIView


router = SimpleRouter()
router.register('', NewsAPIView, basename='news')


urlpatterns = router.urls