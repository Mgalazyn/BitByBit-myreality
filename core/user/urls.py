from django.urls import path, include
from user import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

router = DefaultRouter()
router.register('users', views.UserViewSet)

app_name = 'user'

urlpatterns = [
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('', include(router.urls)),
]