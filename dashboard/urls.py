from django.urls import path, include
from . import views

app_name='dashboard'

urlpatterns = [
    path('',views.index, name='index'),
    path('delete/', views.deleteUsers, name='delete'),
    path('promote/<int:pk>/', views.promoteUser, name='promote'),
    path('add-category/', views.add_category, name='add_category'),
    path('items/', include('item.urls')),
]
