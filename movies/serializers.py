from rest_framework import serializers
from .models import Movie
from .models import RatingChoices


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10,
        required=False
    )
    synopsis = serializers.CharField(
        allow_blank=True,
        required=False
        )
    rating = serializers.ChoiceField(
        required=False, 
        allow_blank=False,
        choices=RatingChoices.choices,
        )

    added_by = serializers.SerializerMethodField("get_email")

    def get_email(self, movie: Movie):
        return movie.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
