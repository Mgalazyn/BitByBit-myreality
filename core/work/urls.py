from django.urls import path, include
from work import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('works', views.WorkViewSet)

app_name = 'work'

urlpatterns = [
    path('', include(router.urls)),
]