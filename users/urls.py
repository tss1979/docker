
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, recover_password, UsersListView, block_user, unblock_user

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('recover_password/', recover_password, name='recover_password'),
    path('', UsersListView.as_view(), name='users'),
    path('block/<int:pk>', block_user, name='block_user'),
    path('unblock/<int:pk>', unblock_user, name='block_user'),
]