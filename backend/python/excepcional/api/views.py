from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.models import Environment, Event, Application, User

from api.serializers import EnvironmentModelSerializer
from api.serializers import EventModelSerializer
from api.serializers import ApplicationModelSerializer
from api.serializers import UserModelSerializer


class EnvironmentList(APIView):
    """
    List all environments, or create a new environment.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        environments = Environment.objects.all()
        serializer = EnvironmentModelSerializer(environments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EnvironmentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnvironmentDetail(APIView):
    """
    Retrieve, update or delete a environment instance.
    """
    def get_object(self, pk):
        try:
            return Environment.objects.get(pk=pk)
        except Environment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        environment = Environment.objects.get(pk=pk)
        serializer = EnvironmentModelSerializer(environment)

        return Response(serializer.data)

    def put(self, request, pk):
        environment = self.get_object(pk)
        serializer = EnvironmentModelSerializer(environment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        environment = self.get_object(pk)
        environment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventList(APIView):
    """
    List all events, or create a new events.
    """
    def get(self, request):
        events = Event.objects.all()
        serializer = EventModelSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    """
    Retrieve, update or delete a events instance.
    """
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        events = Event.objects.get(pk=pk)
        serializer = EventModelSerializer(events)

        return Response(serializer.data)

    def put(self, request, pk):
        events = self.get_object(pk)
        serializer = EventModelSerializer(events, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        events = self.get_object(pk)
        events.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApplicationList(APIView):
    """
    List all applications, or create a new applications.
    """
    def get(self, request):
        applications = Application.objects.all()
        serializer = ApplicationModelSerializer(applications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApplicationModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApplicationDetail(APIView):
    """
    Retrieve, update or delete a applications instance.
    """
    def get_object(self, pk):
        try:
            return Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        applications = Application.objects.get(pk=pk)
        serializer = ApplicationModelSerializer(applications)

        return Response(serializer.data)

    def put(self, request, pk):
        applications = self.get_object(pk)
        serializer = ApplicationModelSerializer(applications, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        applications = self.get_object(pk)
        applications.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetail(APIView):
    """
    Retrieve, update or delete a users instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        users = User.objects.get(pk=pk)
        serializer = UserModelSerializer(users)

        return Response(serializer.data)

    def put(self, request, pk):
        users = self.get_object(pk)
        serializer = UserModelSerializer(users, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        users = self.get_object(pk)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
