from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView, status
from .models import User
from .serializers import UserSerializer


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
