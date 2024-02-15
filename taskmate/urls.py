from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todoList_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoList_views.index, name ='index'),
    path('todolist/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('contact', todoList_views.contact, name ='contact'),
    path('about', todoList_views.about, name ='about'),
]
