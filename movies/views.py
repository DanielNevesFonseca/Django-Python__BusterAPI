from rest_framework.views import APIView, status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from .permissions import MyCustomMoviePermissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomMoviePermissions]

    def post(self, req: Request) -> Response:
        movie_serialized = MovieSerializer(data=req.data)
        movie_serialized.is_valid(raise_exception=True)
        movie_serialized.save(user=req.user)
        return Response(movie_serialized.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        movies = Movie.objects.all()
        movies_validated = MovieSerializer(movies, many=True)
        return Response(movies_validated.data, status.HTTP_200_OK)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomMoviePermissions]

    def get(self, req: Request, movie_id: int) -> Response:
        try:
            found_movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": "Movie not found."}, status.HTTP_404_NOT_FOUND
            )
        serializer = MovieSerializer(found_movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, req: Request, movie_id: int) -> Response:
        try:
            found_movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": "Movie not found."}, status.HTTP_404_NOT_FOUND
            )
        found_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
