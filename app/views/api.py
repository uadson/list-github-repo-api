from app.serializers import ListRepoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from app.models import Repository


class ListRepoApiView(APIView):
	def get(self, request):
		repos = Repository.objects.all()
		serialized = ListRepoSerializer(repos, many=True)
		return Response(serialized.data)


@api_view(['GET'])
def get_repos(request):
	search = request.query_params.get('search', None)
	data_repo = request.query_params.get('dataRepo', None)

	repos = Repository.objects.all()
