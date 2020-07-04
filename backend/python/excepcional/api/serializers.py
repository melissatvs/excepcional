from rest_framework import serializers
from api.models import Environment, Application, User, Event


class EnvironmentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environment
        fields = [
            'id',
            'name',
            'description'
        ]


class ApplicationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = [
            'id',
            'name',
            'environment',
            'user'
        ]


class UserFullModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'e_mail',
            'password',
            'date_created'
        ]


class UserViewModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'e_mail',
            'date_created'
        ]


class EventModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'datetime',
            'user_name',
            'level',
            'ip_address',
            'message',
            'application',
            'environment',
            'occurrences'
        ]
