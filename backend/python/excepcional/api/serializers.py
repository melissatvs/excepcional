from rest_framework import serializers

from api.models import Environment
from api.models import Application
from api.models import User
from api.models import Event


class EnvironmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = [
            'name',
            'description'
        ]


class ApplicationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'name',
            'environment'
        ]


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'e_mail',
            'password',
            'date_created',
            'application'
        ]


class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'datetime',
            'level',
            'ip_address',
            'message',
            'application',
            'environment',
            'user'
        ]
