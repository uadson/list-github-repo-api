from app.serializers import ListRepoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import Repository


class ListRepoApiView(APIView):
	def get(self, request):
		repos = Repository.objects.all()
		serialized = ListRepoSerializer(repos, many=True)
		return Response(serialized.data)
