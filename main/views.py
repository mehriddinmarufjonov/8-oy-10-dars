from rest_framework.viewsets import ModelViewSet
from .serializers import LessonSerializer, LessonVideoSerializer
from .models import Lesson ,LessonVideo
from rest_framework import permissions



class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.DjangoModelPermissions]



class LessonVideoViewSet(ModelViewSet):
    queryset = LessonVideo.objects.all()
    serializer_class = LessonVideoSerializer
    permission_classes = [permissions.DjangoModelPermissions]


