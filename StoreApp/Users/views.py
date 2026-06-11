from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from .serializers import UserSerializer, LoginUserSerializer, GetUserSerializer


class ListUsers(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format = None):
        users =  User.objects.all()
        user_serializer = GetUserSerializer(users, many=True)
        return Response(user_serializer.data,status=status.HTTP_200_OK)

class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class LoginUser(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request, format= None):
        serializer = LoginUserSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username = username, password=password)
            
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message' : "Login operation successful."
            }, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Invalid credentials entered"}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,format=None):
        serializer_class = GetUserSerializer(request.user)
        return Response(serializer_class.data,status=status.HTTP_200_OK)