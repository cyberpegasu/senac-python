from django.urls import path

from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visitors/', views.visitors, name='visitors'),
    path('visitors/create/', views.create_visitor, name='create_visitor'),
    path('visitors/update/<int:id>/', views.update_visitor, name='update_visitor'),
    path('visitors/delete/<int:id>/', views.delete_visitor, name='delete_visitor'),
    path('visitors/estatisticas/', views.estatisticas, name='estatisticas')
]