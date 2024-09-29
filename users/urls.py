from django.urls import path
from users.apps import UsersConfig

from users.views import UserRegisterView, Login, Logout, RestorePassword

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('restore/', RestorePassword.as_view(), name='restore'),

]
