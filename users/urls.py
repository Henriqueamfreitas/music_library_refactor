from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CreateUserView, RetrieveUpdateDestroyUserView

urlpatterns = [
    path("users/", CreateUserView.as_view()),
    path("users/<int:pk>/", RetrieveUpdateDestroyUserView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
