from django.urls import path
from .views import InventoryItemsView,InventoryItemsUpdateView
urlpatterns = [
    path('items/',InventoryItemsView.as_view(),name='inventory_items'),
    path('items/<int:pk>/',InventoryItemsUpdateView.as_view(),name='inventory_items_update'),
]
