from rest_framework import serializers
from apikey.authentication.models import ApiKey


class InputApiKeySerializer(serializers.Serializer):
    company_id = serializers.IntegerField()


class OutputApiKeySerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiKey
        fields = ['api_key']