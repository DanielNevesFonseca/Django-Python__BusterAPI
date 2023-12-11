from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies_orders.serializers import MovieOrderSerializer
from movies.models import Movie
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, req: Request, movie_id: int) -> Response:
        found_movie = get_object_or_404(Movie.objects.all(), pk=movie_id)
        movie_serialized = MovieOrderSerializer(data=req.data)
        movie_serialized.is_valid(raise_exception=True)
        movie_serialized.save(movie=found_movie, user=req.user)
        return Response(movie_serialized.data, status.HTTP_201_CREATED)
