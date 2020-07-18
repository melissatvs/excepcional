import jwt
from rest_framework import authentication, exceptions
from excepcional.settings import SECRET_USER, SECRET_APP


class UserAuthentication(authentication.BaseAuthentication):

    user_id = 0

    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            raise exceptions.AuthenticationFailed(
                'Não foi informado token de acesso do usuário'
            )

        token = token.replace('Bearer ', '')
        response = CustomAuthentication.verify_token(token, SECRET_USER)

        self.user_id = response[0].get('user_id')

        return response


class ApplicationAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            raise exceptions.AuthenticationFailed(
                'Não foi informado token de acesso da aplicação'
            )

        token = token.replace('Bearer ', '')

        return CustomAuthentication.verify_token(token, SECRET_APP)


class CustomAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

    def create_token(payload: object, secret: str) -> str:
        try:
            return jwt.encode(payload, secret).decode('utf-8')
        except Exception as error:
            raise exceptions.AuthenticationFailed(
                'Falha na autenticação ' + str(error)
            )

    def verify_token(token: str, secret: str):
        try:
            return (jwt.decode(token, secret), None)
        except Exception as error:
            raise exceptions.AuthenticationFailed(
                'Falha na autenticação ' + str(error)
            )
