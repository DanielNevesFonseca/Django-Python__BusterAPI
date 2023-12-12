from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView, status

from users.permissions import IsUserOwner
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        users = User.objects.all()
        users_validate = UserSerializer(users, many=True)
        return Response(users_validate.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner]

    def get(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User.objects.filter(id=user_id))
        self.check_object_permissions(request, found_user)
        user_serializer = UserSerializer(found_user)
        return Response(user_serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User.objects.filter(id=user_id))
        self.check_object_permissions(request, found_user)
        serializer = UserSerializer(
            found_user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = UserSerializer(found_user)
        return Response(serializer.data, status.HTTP_200_OK)
