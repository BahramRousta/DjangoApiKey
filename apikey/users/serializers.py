from rest_framework import serializers


class LoginInputSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)


class LoginOutputSerializer(serializers.ModelSerializer):
    refresh_token = serializers.CharField(max_length=250)
    access_token = serializers.CharField(max_length=250)
