from rest_framework import serializers

from app.models import Repository


class ListRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'