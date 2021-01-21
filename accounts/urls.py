from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url('register/', views.register_view, name="register"),
    url('login/', views.login_view, name="login"),
    url('profile/', views.profile_view, name="profile"),
    url('logout/', views.logout_view, name="logout")
]
