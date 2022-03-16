# Django imports
from django.urls import path

# Local imports
from movies.views import (
  ListCreateMoviesAPIView, 
  DetailMoviesAPIView
  )

app_name = 'movies'

urlpatterns = [
    path('', ListCreateMoviesAPIView.as_view(), name = 'listcreate'),
    path('<int:pk>', DetailMoviesAPIView.as_view(), name = 'detailcreate'),
]