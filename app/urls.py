from django.urls import path
from app.views.api import ListRepoApiView

from app.views.home import HomeView


app_name = 'app'

urlpatterns = [
	# Home
	path('', HomeView.as_view(), name='home'),

	# API
	path('api/repos/', ListRepoApiView.as_view(), name='api_repos'),
]