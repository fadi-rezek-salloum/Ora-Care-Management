from django.urls import path

from . import views

urlpatterns = [
    path('male-list/', views.maleList, name='male-list'),
    path('female-list/', views.femaleList, name='female-list'),

    path('search/', views.search , name='search'),
    path('accounting/', views.accounting , name='accounting'),

    path('profile/<str:id>/', views.profile, name='profile'),
]