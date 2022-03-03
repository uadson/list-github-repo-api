from app.serializers import ListRepoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import Repository


class ListRepoApiView(APIView):
    def get(self, request):
        repos = Repository(
            "usuario",
            "nome do repositorio",
            "url do repositorio",
            "status do repo",
            "quantidade commits",
            "último commit",
            "linguagens utilizadas"
        )

        serialized = ListRepoSerializer(repos, many=True)
        return Response(serialized)
