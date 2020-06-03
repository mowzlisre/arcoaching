from django.urls import path
from django.contrib.auth import views as v

urlpatterns = [
    path('login/', v.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', v.LogoutView.as_view(), name='logout')
]
