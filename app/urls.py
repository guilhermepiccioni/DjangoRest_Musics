from django.urls import path

from . import views


urlpatterns = [
    path('seed-track/', views.TrackSeedView.as_view(), name="seed_track"),
    path('recent-tracks/', views.RecentTracksListView.as_view(), name="recent_tracks"),
    path('artists/', views.ArtistListView.as_view(), name="artists"),
]
