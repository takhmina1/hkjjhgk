from django.urls import path
from . import views

urlpatterns = [
    path('update-exchange-data/', views.update_exchange_data, name='update_exchange_data'),
    # Другие URL-адреса вашего приложения здесь...
]
