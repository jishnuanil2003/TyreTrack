from django.urls import path
from .views import BillView

urlpatterns = [
   path('inventory/bill/',BillView.as_view(),name="bill") 
]
