from django.urls import path

from app.views.home import HomeView
from app.views.api import ListRepoApiView


app_name = 'app'

urlpatterns = [
	# Home
	path('', HomeView.as_view(), name='home'),

	# API
	path('api/repos/', ListRepoApiView.as_view(), name='api_repos'),
	
]