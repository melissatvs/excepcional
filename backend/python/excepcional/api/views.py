from datetime import datetime
from django.http import Http404, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from excepcional.settings import SECRET_USER, SECRET_APP
from api import authentication as excep_auth
from api.filters import EventOrderingFilter
from api.models import Environment, Event, Application, User
from api.resources import api_response
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
    authentication_classes = (excep_auth.UserAuthentication,)

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
    authentication_classes = (excep_auth.UserAuthentication,)

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


class EventList(generics.ListAPIView):
    """
    get:
      Retorna uma lista com os eventos não arquivados
    """
    authentication_classes = (excep_auth.ApplicationAuthentication,)
    serializer_class = EventModelSerializer

    queryset = Event.objects.filter(archived=False)
    filter_backends = [DjangoFilterBackend, EventOrderingFilter]
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return api_response(
            'Não foi possível inserir o evento!',
            status.HTTP_400_BAD_REQUEST
        )


class EventDetail(APIView):
    """
    Exclusão, edição e detalhamento de evento
    """
    authentication_classes = (excep_auth.UserAuthentication,)

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

        ---

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
    authentication_classes = (excep_auth.UserAuthentication,)

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
    authentication_classes = (excep_auth.UserAuthentication,)

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


class ApplicationToken(APIView):
    """
    Geração de token para aplicação
    """

    def get_object(self, pk, user_id):
        """
        Busca a aplicação pela chave
        """
        try:
            return Application.objects.get(pk=pk, user__id=user_id)
        except Application.DoesNotExist:
            raise Http404

    def post(self, request):
        """
        Gera token de acesso para aplicação
        """
        application_id = request.data.get('application_id')
        user_id = request.data.get('user_id')

        application = self.get_object(application_id, user_id)

        try:
            token = excep_auth.CustomAuthentication.create_token({
                'application_id': application.id,
                'user_id': application.user.id
            }, SECRET_APP)

            return api_response({'token': token}, status.HTTP_201_CREATED)
        except Exception as error:
            return api_response('Não foi possível gerar a chave de acesso.' +
                                ' Erro: ' + str(error),
                                status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    authentication_classes = (excep_auth.UserAuthentication,)

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
    authentication_classes = (excep_auth.UserAuthentication,)

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


class UserToken(APIView):
    """
    Geração de token para usuário
    """

    def get_object(self, pk, password, application_id):
        """
        Busca o usuário pela chave
        """
        try:
            return User.objects.get(pk=pk,
                                    password=password,
                                    application__id=application_id)
        except User.DoesNotExist:
            raise Http404

    def post(self, request):
        """
        Gera token de acesso para usuário
        """
        id = request.data.get('user_id')
        password = request.data.get('user_password')
        application_id = request.data.get('application_id')

        user = self.get_object(id, password, application_id)

        token = excep_auth.CustomAuthentication.create_token({
                'user_id': user.id,
                'user_password': user.password,
                'application_id': application_id
            }, SECRET_USER)

        if not token:
            return api_response('Não foi possível gerar a chave de acesso.',
                                status.HTTP_400_BAD_REQUEST)

        try:
            data = {
                'token': token
            }

            return JsonResponse(data, status.HTTP_201_CREATED)
            # return api_response(data, status.HTTP_201_CREATED)
        except Exception as error:
            return api_response('Não foi possível gerar a chave de acesso.' +
                                ' Erro: ' + str(error),
                                status.HTTP_400_BAD_REQUEST)
