from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from user import services
from user.models import StoreUser


class UserView(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        password = serializers.CharField()
        email = serializers.EmailField()
        birth_date = serializers.DateField(required=False)
        cpf = serializers.CharField()
        gender = serializers.CharField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = StoreUser
            fields = ("id", "email")

    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        user = services.user_create(**input_serializer.validated_data)
        token = services.user_get_token(user=user)

        return Response(
            {
                "token": token,
                "user": self.OutputSerializer(instance=user).data,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField(required=True)
        password = serializers.CharField(required=True)

    class OutputSerializer(serializers.ModelSerializer):
        email = serializers.SerializerMethodField()
        get_email = lambda _, obj: obj.email

        class Meta:
            model = StoreUser
            fields = (
                "id",
                "email",
            )

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = services.user_login(**serializer.validated_data)
        token = services.user_get_token(user=user)

        return Response(
            {
                "token": token,
                "user": self.OutputSerializer(instance=user).data,
            },
            status=status.HTTP_200_OK,
        )
