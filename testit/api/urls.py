# todo/todo_api/urls.py : API urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('printers/curent_user', show_all_user_printers),
    path('printers', show_all_printers),
    path('printers/<int:id>', get_printer),
    path('printers/create', create_printer),
    path('task', show_all_user_tasks),
    path('task/create', create_task)
]