from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from .models import Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class TrackSeedSerializer(serializers.Serializer):
    tracks = serializers.FileField(
        validators=[FileExtensionValidator(['json'])])


class ArtistSerializer(serializers.ModelSerializer):
    total_tracks = serializers.SerializerMethodField()
    recently_played_track = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = ['artist', 'total_tracks', 'recently_played_track']

    @staticmethod
    def get_total_tracks(obj):
        return Track.objects.filter(artist=obj.artist).count()

    @staticmethod
    def get_recently_played_track(obj):
        return Track.objects.filter(artist=obj.artist).order_by('-last_play').first().title
