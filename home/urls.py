from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name="Home"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register, name="register"),
    path('record/<int:pk>', views.record, name="record"),
    path('record/<int:pk>/delete', views.delete_rec, name="delete"),
    path('record/<int:pk>/edit', views.edit_rec, name="edit"),
    path('search/', views.search_rec, name="search")
]
