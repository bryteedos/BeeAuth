from django.urls import path
from.import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.loginuser, name='login'),
    path('logout/',views.logoutuser, name='logout'),
    path('register/',views.registeruser, name='register'),
    path('editprofile/',views.editprofile, name='editprofile'),
    path('changepassword/',views.changepassword, name='changepassword'),
]
