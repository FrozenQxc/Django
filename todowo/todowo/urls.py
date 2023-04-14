from django.urls import path
from django.contrib import admin

from todo.views import (
    home, 
    signup_user,
    current_todos,
    logout_user,
    login_user,
    create_todo,
    viewtodo
)

# The urlpatterns for the project
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    
    # Auth URLs
    path('signup/', signup_user, name='signup_user'),
    path('logout/', logout_user, name='logout_user'),
    path('login/', login_user, name='login_user'),
    
    # Todo URLs
    path('create/', create_todo, name='create_todo'),
    path('current/', current_todos, name='current_todos'),
    path('todo/<int:todo_pk>', viewtodo, name='viewtodo'),
]
