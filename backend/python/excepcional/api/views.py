from django.http import Http404

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema

# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

from api.models import Environment, Event, Application, User

from api.serializers import EnvironmentModelSerializer
from api.serializers import EventModelSerializer
from api.serializers import ApplicationModelSerializer
from api.serializers import UserFullModelSerializer
from api.serializers import UserViewModelSerializer


class EnvironmentListFiltered(generics.ListAPIView):
    model = Environment
    serializer_class = EnvironmentModelSerializer
    
    def get_queryset(self):
        """
        Retorna uma lista com todos ambientes
        """
        queryset = self.model.objects.all()

        return queryset


class EnvironmentCreate(APIView):
    def post(self, request):
        """
        Cria um novo ambiente
        """
        serializer = EnvironmentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnvironmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Environment.objects.get(pk=pk)
        except Environment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        environment = self.get_object(pk)
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


class EventListFiltered(generics.ListAPIView):
    model = Event
    serializer_class = EventModelSerializer

    def get_queryset(self):
        """
        parameters:
        - in: query
            name: application
            required: false
            schema:
            description: 'Id da Aplicação'
            title: ''
            type: integer
        - in: query
            name: environment
            required: false
            schema:
            description: 'Id do Ambiente'
            title: ''
            type: integer
        """

        queryset = self.model.objects.all()
        application = self.request.query_params.get('application')
        environment = self.request.query_params.get('environment')

        ordering_fields = ['level']

        if application:
            queryset = queryset.filter(application__id=application)

        if environment:
            queryset = queryset.filter(environment__id=environment)

        return queryset

    def post(self, request):
        """
        Cria um novo evento
        """
        serializer = EventModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retorna o evento
        """
        event = self.get_object(pk)
        serializer = EventModelSerializer(event)

        return Response(serializer.data)

    def delete(self, request, pk):
        """
        Exclui o evento
        """

        event = self.get_object(pk)
        event.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ApplicationList(APIView):
    """
    List all applications, or create a new application.
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
    Retrieve, update or delete a application instance.
    """
    def get_object(self, pk):
        try:
            return Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        application = self.get_object(pk)
        serializer = ApplicationModelSerializer(application)

        return Response(serializer.data)

    def put(self, request, pk):
        application = self.get_object(pk)
        serializer = ApplicationModelSerializer(
            application,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        application = self.get_object(pk)
        application.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    def post(self, request):
        """
        Cria um usuário
        """
        serializer = UserFullModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        users = self.get_object(pk)
        serializer = UserViewModelSerializer(users)

        return Response(serializer.data)

    def put(self, request, pk):
        users = self.get_object(pk)
        serializer = UserFullModelSerializer(users, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        users = self.get_object(pk)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
