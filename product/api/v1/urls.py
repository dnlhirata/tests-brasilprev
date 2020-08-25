from django.urls import path

from .views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path("", ProductCreateView.as_view(), name="product-create-view"),
    path("list/", ProductListView.as_view(), name="product-list-view"),
    path("detail/", ProductDetailView.as_view(), name="product-detail-view"),
    path("update/", ProductUpdateView.as_view(), name="product-update-view"),
    path("delete/", ProductDeleteView.as_view(), name="product-delete-view"),
]
