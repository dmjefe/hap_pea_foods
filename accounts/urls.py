from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    url('register/', views.register_view, name="register"),
    url('profile/', views.profile_view, name="profile"),
    url('login/', views.login_view, name="login"),
    url('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
