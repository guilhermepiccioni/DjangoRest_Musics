import json
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from .serializers import TrackSeedSerializer, TrackSerializer, ArtistSerializer
from .models import Track


class TrackSeedView(generics.CreateAPIView):
    serializer_class = TrackSeedSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tracks = json.loads(request.data.get('tracks').read())

        for track in tracks:
            Track.objects.create(**track)

        return Response(data={'status': 'success'}, status=status.HTTP_201_CREATED)


class TrackViewSets(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', 'title', 'artist')
    search_fields = ('id', 'title', 'artist')


class RecentTracksListView(generics.ListAPIView):
    serializer_class = TrackSerializer
    queryset = Track.objects.order_by('-last_play')[:100]


class ArtistListView(generics.ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Track.objects.all().distinct()
