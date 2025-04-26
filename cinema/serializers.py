from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=100,
        required=True,
        error_messages={
            "required": "Title is required.",
            "max_length": "Title cannot exceed 100 characters."
        }
    )
    description = serializers.CharField(
        required=True,
        error_messages={
            "required": "Description is required.",
        }
    )
    duration = serializers.IntegerField(
        required=True,
        error_messages={
            "required": "Duration is required.",
        }
    )

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance
