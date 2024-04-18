from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner, IsModerator, IsNotModerator
from .models import Lesson
from .serializers import CourseSerializer, LessonSerializer

# Представления для курсов

from rest_framework import viewsets
from courses.models import Course


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModerator, IsOwner]

    def perform_create(self, serializer):
        # При создании курса добавляем текущего пользователя как владельца
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated and IsNotModerator]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsModerator, IsOwner]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsModerator, IsOwner]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, IsModerator, IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]


# Представления для уроков
class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator, IsOwner]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator or IsOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated and IsNotModerator]

    def perform_create(self, serializer):
        # При создании урока добавляем текущего пользователя как владельца
        serializer.save(owner=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner or IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]


#
# class CourseListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseCreateAPIView(generics.CreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseUpdateAPIView(generics.UpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseDestroyAPIView(generics.DestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer