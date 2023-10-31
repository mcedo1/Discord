from django.urls import path
from . import views  as v 


urlpatterns=[
    path('',v.home,name='home'),
    path('room/<str:pk>',v.room, name='room'),
    path('create-room/',v.createRoom,name='create-room'),
    path('update-room/<str:pk>',v.updateRoom,name='update-room'),
    path('delete-room/<str:pk>',v.deleteRoom,name='delete-room'),
    path('login/',v.loginPage,name='login'),
    path('logout/',v.logoutUser,name='logout'),
    path('register/',v.registerPage,name='register'),
    path('delete-message/<str:pk>',v.deleteMessage,name='delete-message'),
    path('profile/<str:pk>', v.userProfile,name='user-profile'),
    path('update-user/',v.updateUser,name='update-user'),
    path('topics/',v.topicsPage,name='topics'),
    path('activity/',v.activityPage,name='activity')


]












