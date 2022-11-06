from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('', views.account, name='account'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-profile/', views.change_profile, name='change-profile'),
    path('password/', views.pass_change, name='pass-change')
]

