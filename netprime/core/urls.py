from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'), 
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('movie/<str:pk>/', views.movie, name='movie'),
    path('my-list/', views.my_list, name='my-list'),
    path('add-to-list', views.add_to_list, name='add-to-list'),
    path('search', views.search, name='search'),
    path('remove-from-list', views.remove_from_list, name='remove-from-list'),
    path('genre/<str:genre>/', views.genre, name='genre'),
]