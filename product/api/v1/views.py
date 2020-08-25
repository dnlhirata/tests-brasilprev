from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.pagination import PageNumberPagination
from product import services
from product.models import Product
from store.mixins import AuthenticationMixin, PaginatorMixin


class ProductCreateView(AuthenticationMixin, APIView):
    authenticated_methods = ('POST',)

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        description = serializers.CharField(required=False)
        price = serializers.FloatField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ('id', 'name', 'description', 'price')

    def post(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        product = services.product_create(**input_serializer.validated_data)

        return Response(self.OutputSerializer(product).data, status=status.HTTP_201_CREATED)


class ProductListView(APIView, PaginatorMixin):
    pagination_class = PageNumberPagination

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ('id', 'name', 'description', 'price')

    def get(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.query_params)
        input_serializer.is_valid(raise_exception=True)

        products = services.product_get_list(**input_serializer.validated_data)

        page = self.paginate_queryset(products)
        if page is not None:
            return self.get_paginated_response(self.OutputSerializer(page, many=True).data)

        return Response(self.OutputSerializer(page, many=True).data)


class ProductDetailView(APIView):
    class InputSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=True)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ('id', 'name', 'description', 'price')

    def get(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.query_params)
        input_serializer.is_valid(raise_exception=True)

        product = services.product_get_detail(**input_serializer.validated_data)

        return Response(self.OutputSerializer(product).data)


class ProductUpdateView(AuthenticationMixin, APIView):
    authenticated_methods = ('PATCH',)

    class InputSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=True)
        name = serializers.CharField(required=False)
        description = serializers.CharField(required=False)
        price = serializers.FloatField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ('id', 'name', 'description', 'price')

    def patch(self, request, *args, **kwargs):
        data = {**request.data, 'id': request.query_params.get('id')}
        input_serializer = self.InputSerializer(data=data)
        input_serializer.is_valid(raise_exception=True)

        product = services.product_update(**input_serializer.validated_data)

        return Response(self.OutputSerializer(product, many=False).data)


class ProductDeleteView(AuthenticationMixin, APIView):
    authenticated_methods = ('DELETE',)

    class InputSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=True)

    def delete(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.query_params)
        input_serializer.is_valid(raise_exception=True)

        services.product_delete(**input_serializer.validated_data)

        return Response(status=status.HTTP_200_OK)
