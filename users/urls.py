from .views import UserListApiView, UserDetailApiView, UserCreateAPIView, GetUserByToken, obtain_auth_token, \
    CustomAuthToken
from django.urls import path, re_path

urlpatterns = [
    path('', UserListApiView.as_view()),
    path('user-by-token/', GetUserByToken.as_view()),
    path('<int:pk>/', UserDetailApiView.as_view()),
    path('register/', UserCreateAPIView.as_view()),
    # re_path(r'^api-token-auth/', obtain_auth_token),
    path('token/', CustomAuthToken.as_view()),

]
