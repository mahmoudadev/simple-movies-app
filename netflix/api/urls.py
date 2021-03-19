from django.urls import path
from .views import index, create, MovieList, CreateMovie, UpdateMovie, api_signup
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("login/", obtain_auth_token),
    path("signup", api_signup),
    path("", index),
    path("create", create),
    path("list/", MovieList.as_view()),
    path("store/", CreateMovie.as_view()),
    path("update/<int:pk>/", UpdateMovie.as_view())
]