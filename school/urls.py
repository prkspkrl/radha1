from django.contrib import admin
from django.urls import path
from . import views
from .views import StaffListView, StaffDetailView, StaffCreateView, StaffUpdateView, StaffDeleteView


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home', views.HomeView.as_view()),
    path('', views.about.as_view(), name='about'),
    path('about', views.about.as_view()),
    path('staff/', StaffListView.as_view(), name='staff_list'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
    path('staff/create/', StaffCreateView.as_view(), name='staff_create'),
    path('staff/<int:pk>/update/', StaffUpdateView.as_view(), name='staff_update'),
    path('staff/<int:pk>/delete/', StaffDeleteView.as_view(), name='staff_delete'),
    
]


