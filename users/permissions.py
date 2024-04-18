from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверяем, является ли пользователь модератором
        if request.user.groups.filter(name='Moderators').exists():
            return True
        # Проверяем, имеет ли пользователь доступ к конкретному курсу/уроку, если это запрос на просмотр или обновление
        elif view.action in ['retrieve', 'update', 'destroy']:
            if view.kwargs.get('pk'):
                course_or_lesson = view.get_queryset().filter(pk=view.kwargs['pk']).first()
                return course_or_lesson and course_or_lesson.owner == request.user
            return False
        # Для всех остальных случаев (создание нового курса/урока или получение списка)
        return True


class IsOwnerOrModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Если пользователь является модератором, разрешаем доступ
        if request.user.groups.filter(name='moderators').exists():
            return True
        # Если пользователь не модератор и объект принадлежит ему, разрешаем доступ
        return obj.owner == request.user