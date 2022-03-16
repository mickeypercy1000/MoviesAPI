from rest_framework import generics
from movies.serializers import MoviesAPISerializer
from movies.models import MoviesAPI


class ListCreateMoviesAPIView(generics.ListCreateAPIView):
    queryset = MoviesAPI.objects.all()
    serializer_class = MoviesAPISerializer

class DetailMoviesAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoviesAPI.objects.all()
    serializer_class = MoviesAPISerializer