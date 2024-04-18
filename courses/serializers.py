from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from courses.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'preview', 'video_link', 'course', 'owner']


class SimpleLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'preview', 'description', 'num_of_lessons', 'lessons', 'owner']


class CourseSerializer(serializers.ModelSerializer):
    num_of_lessons = serializers.SerializerMethodField()
    lessons = SimpleLessonSerializer(many=True, read_only=True)

    def get_num_of_lessons(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'preview', 'description', 'num_of_lessons', 'lessons']
