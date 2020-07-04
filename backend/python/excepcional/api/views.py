from datetime import datetime
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from api.resources import api_response
from api.models import Environment, Event, Application, User
from api.serializers import (
    EnvironmentModelSerializer,
    EventModelSerializer,
    ApplicationModelSerializer,
    UserFullModelSerializer,
    UserViewModelSerializer,
)


class EnvironmentList(APIView):
    """
    Listagem e criação de ambientes
    """

    def get(self, request):
        """
        Retorna uma lista com todos ambientes
        """
        environments = Environment.objects.all()
        serializer = EnvironmentModelSerializer(environments, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Cria um novo ambiente
        """
        serializer = EnvironmentModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return api_response(
            'Não foi possível criar o ambiente',
            status.HTTP_400_BAD_REQUEST
        )


class EnvironmentDetail(APIView):
    """
    Exclusão, edição e detalhamento de ambiente
    """

    def get_object(self, pk):
        """
        Busca o ambiente pela chave
        """
        try:
            return Environment.objects.get(pk=pk)
        except Environment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retorna o ambiente
        """
        environment = self.get_object(pk)
        serializer = EnvironmentModelSerializer(environment)

        return Response(serializer.data)

    def put(self, request, pk):
        """
        Altera o ambiente
        """
        environment = self.get_object(pk)
        serializer = EnvironmentModelSerializer(environment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return api_response(
            'Não foi possível editar o ambiente!',
            status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """
        Exclui o ambiente
        """
        environment = self.get_object(pk)
        environment.delete()

        return api_response('Ambiente excluído!', status.HTTP_204_NO_CONTENT)


class EventListFiltered(generics.ListAPIView):
    """
    get:
      Retorna uma lista com os eventos não arquivados
    """
    queryset = Event.objects.filter(archived=False)
    model = Event
    serializer_class = EventModelSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['application', 'environment']
    ordering_fields = ['datetime', 'level']
    ordering = ['datetime']

    def post(self, request):
        """
        Insere um novo evento
        """
        serializer = EventModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return api_response('Evento inserido!', status.HTTP_201_CREATED)

        return api_response(
            'Não foi possível inserir o evento!',
            status.HTTP_400_BAD_REQUEST
        )


class EventDetail(APIView):
    """
    Exclusão, edição e detalhamento de evento
    """

    def get_object(self, pk):
        """
        Busca o evento pela chave
        """
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

    def put(self, request, pk):
        """
        Arquiva o evento
        """
        event = self.get_object(pk)

        if event.archived:
            return api_response(
                'Evento já está arquivado!',
                status.HTTP_400_BAD_REQUEST
            )

        event.archived = True
        event.datetime_archived = datetime.now()

        try:
            event.save()
            return api_response('Evento arquivado!', status.HTTP_200_OK)
        except Exception:
            return api_response(
                'Não foi possível arquivar o evento!',
                status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        """
        Exclui o evento
        """

        event = self.get_object(pk)
        event.delete()

        return api_response('Evento excluído!', status.HTTP_204_NO_CONTENT)


class ApplicationList(APIView):
    """
    Listagem e criação de aplicações
    """

    def get(self, request):
        """
        Retorna uma lista com todas aplicações
        """
        applications = Application.objects.all()
        serializer = ApplicationModelSerializer(applications, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Cria uma nova aplicação
        """
        serializer = ApplicationModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return api_response(
            'Não foi possível criar a aplicação',
            status.HTTP_400_BAD_REQUEST
        )


class ApplicationDetail(APIView):
    """
    Exclusão, edição e detalhamento de aplicação
    """
    def get_object(self, pk):
        """
        Busca a aplicação pela chave
        """
        try:
            return Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retorna a aplicação
        """
        application = self.get_object(pk)
        serializer = ApplicationModelSerializer(application)

        return Response(serializer.data)

    def put(self, request, pk):
        """
        Altera a aplicação
        """
        application = self.get_object(pk)
        serializer = ApplicationModelSerializer(
            application,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return api_response(
            'Não foi possível editar a aplicação!',
            status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """
        Exclui a aplicação
        """
        application = self.get_object(pk)
        application.delete()

        return api_response('Aplicação excluída!', status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    """
    Criação de usuário
    """
    def post(self, request):
        """
        Cria um usuário
        """
        serializer = UserFullModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return api_response(
            'Não foi possível criar o usuário',
            status.HTTP_400_BAD_REQUEST
        )


class UserDetail(APIView):
    """
    Exclusão, edição e detalhamento de ambiente
    """

    def get_object(self, pk):
        """
        Busca o usuário pela chave
        """
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retorna o usuário
        """
        users = self.get_object(pk)
        serializer = UserViewModelSerializer(users)

        return Response(serializer.data)

    def put(self, request, pk):
        """
        Altera o usuário
        """
        users = self.get_object(pk)
        serializer = UserFullModelSerializer(users, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return api_response(
            'Não foi possível editar o usuário!',
            status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """
        Exclui o usuário
        """
        users = self.get_object(pk)
        users.delete()

        return api_response('Usuário excluído!', status.HTTP_204_NO_CONTENT)
