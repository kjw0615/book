from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.main),
    path("select/", views.select),
    path("insert/", views.insert),
    path("update/", views.update),
    path("delete/", views.delete),
    path('login/', auth_views.LoginView.as_view(template_name='book_list/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
