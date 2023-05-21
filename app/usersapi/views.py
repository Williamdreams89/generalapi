from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer

class UserRegisterAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()



        return Response({"message":"New User Created Successfully"}, status=status.HTTP_201_CREATED)
