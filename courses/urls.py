from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.apps import CoursesConfig
from courses.views import CoursesViewSet, LessonListCreateAPIView, LessonRetrieveAPIView, LessonCreateAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = CoursesConfig.name

# Создаем маршрутизатор
router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')

urlpatterns = [
    # URL-маршруты для уроков
    path('lessons/', LessonListCreateAPIView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
]

# Добавляем URL-маршруты из маршрутизатора
urlpatterns += router.urls