from django.urls import path, include
from .views import (LessonViewSet, LessonVideoViewSet)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework import routers

router = routers.SimpleRouter()
router.register('lesson', LessonViewSet)
router.register('lesson-video', LessonVideoViewSet)

urlpatterns = [
    path('main/', include(router.urls)),



    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]