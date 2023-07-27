from rest_framework import serializers
from apikey.company.models import Company


class InputCompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class OutputCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name')