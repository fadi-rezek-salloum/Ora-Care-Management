from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<int:month>/<int:day>/', views.home, name='home'),

    path('patient/<pk>/delete/', views.delete_patient, name='delete_patient'),

    path('update-appointment/<int:year>/<int:month>/<int:day>/<int:id>/', views.updateAppointment, name='update-appointment'),
    path('delete-appointment/<int:year>/<int:month>/<int:day>/<int:id>/', views.deleteAppointment, name='delete-appointment'),
]