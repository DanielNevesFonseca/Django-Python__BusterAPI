from rest_framework import serializers
from movies_orders.models import MovieOrder
from movies.models import Movie


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    purchased_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    title = serializers.SerializerMethodField("get_title")
    purchased_by = serializers.SerializerMethodField("get_email")

    def get_title(self, movie_order: MovieOrder):
        return movie_order.movie.title
    
    def get_email(self, movie: Movie):
        return movie.user.email

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)