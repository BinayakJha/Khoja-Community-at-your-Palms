from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('', views.Tabs.index, name='index'),
    path('add_eca/', views.Tabs.add_eca, name='add_eca'),
    path('add_eca_submit/', views.forms.add_eca_submit, name='add_eca_submit'),
    path('eca_apply/<str:name>', views.Tabs.eca_apply, name='eca_apply'),
    path('login/', views.Tabs.login, name='login'),
    path('login_submit/', views.Authentication.login, name='login_submit'),
    path('signup/', views.Tabs.signup, name='signup'),
    path('signup_submit/', views.Authentication.signup, name='signup_submit'),
    path('logout/', views.Authentication.logout, name='logout'),
    # view_eca
    path('view_eca/<str:name>/', views.View.view_eca, name='view_eca'),
    path('eca_apply_submit/', views.Authentication.eca_apply_submit, name='eca_apply_submit'),
]