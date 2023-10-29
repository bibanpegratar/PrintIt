from django.urls import path
from .views import register_user, user_login, user_logout, get_current_user, get_user_by_id

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('current_user/', get_current_user, name='current user'),
    path('<int:user_id>/', get_user_by_id)
]