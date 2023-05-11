from django.urls import path, include
from task import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', views.TaskViewSet)

app_name = 'task'

urlpatterns = [
    path('', include(router.urls)),
]