from django.urls import path 
from . import views as v

urlpatterns=[
    path('',v.getRoutes),
    path('rooms/',v.getRooms),
    path('rooms/<str:pk>',v.getRoom),
]