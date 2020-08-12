from django.urls import path
from . import views

from django.urls import include, path

app_name = 'shop'

urlpatterns = [
    path('item_list', views.IndexView.as_view(), name = 'item_list'),
    path('item_create', views.ItemCreateView.as_view(), name = 'item_create'),
    path('item_detail/<pk>', views.ItemDetailView.as_view(), name = 'item_detail'),
    path('item_delete/<pk>', views.ItemDeleteView.as_view(), name = 'item_delete'),
    path('item_update/<pk>', views.ItemUpdateView.as_view(), name = 'item_update'),
    path('order_request/', views.OrderRequest.as_view(), name = 'order_request'),
]
