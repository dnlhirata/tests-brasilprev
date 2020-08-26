from django.urls import path

from .views import OrderCreateView, OrderListView

urlpatterns = [
    path("", OrderCreateView.as_view(), name="order-create-view"),
    path("list/", OrderListView.as_view(), name="order-list-view"),
]
