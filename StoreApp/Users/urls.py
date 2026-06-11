from django.urls import include, path
from .views import ListUsers, UserDetail, RegisterUser, LoginUser

urlpatterns = [
    path("get-users/", ListUsers.as_view()),
    path("details/",UserDetail.as_view()),
    path("register/", RegisterUser.as_view()),
    path('login/', LoginUser.as_view()),
]
