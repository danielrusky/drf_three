from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Lesson
from .serializers import CourseSerializer, LessonSerializer

# Представления для курсов

from rest_framework import viewsets
from courses.models import Course


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # При создании курса добавляем текущего пользователя как владельца
        serializer.save(owner=self.request.user)


# Представления для уроков
class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # При создании урока добавляем текущего пользователя как владельца
        serializer.save(owner=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


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