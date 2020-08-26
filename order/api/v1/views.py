from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.pagination import PageNumberPagination

from order.models import Order
from order import services
from product.models import Product
from store.mixins import AuthenticationMixin, PaginatorMixin


class OrderCreateView(AuthenticationMixin, APIView):
    authenticated_methods = ('POST',)

    class InputSerializer(serializers.Serializer):
        class InputSerializer(serializers.Serializer):
            product = serializers.IntegerField(required=True)
            quantity = serializers.IntegerField(required=True)

        items = InputSerializer(many=True)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = ('id',)

    def post(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        product = services.order_create(user=request.user, **input_serializer.validated_data)

        return Response(self.OutputSerializer(product).data, status=status.HTTP_201_CREATED)


class OrderListView(AuthenticationMixin, PaginatorMixin, APIView):
    authenticated_methods = ('GET',)
    pagination_class = PageNumberPagination

    class OutputSerializer(serializers.Serializer):
        class OutputSerializer(serializers.Serializer):
            class OutputSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Product
                    fields = ('name', )

            product = OutputSerializer(many=False)
            quantity = serializers.IntegerField()

        order = serializers.IntegerField()
        products = OutputSerializer(many=True)
        date = serializers.DateTimeField()

    def get(self, request, *args, **kwargs):
        orders = services.order_get_orders_from_user(user=request.user)

        page = self.paginate_queryset(orders)
        if page is not None:
            return self.get_paginated_response(self.OutputSerializer(page, many=True).data)

        return Response(self.OutputSerializer(page, many=True).data)

