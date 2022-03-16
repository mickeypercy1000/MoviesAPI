from rest_framework import serializers
from movies.models import MoviesAPI

class MoviesAPISerializer(serializers.ModelSerializer):
  class Meta:
    model = MoviesAPI
    fields = '__all__'