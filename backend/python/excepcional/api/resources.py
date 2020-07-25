from django.http import JsonResponse
from rest_framework import status


def api_response(message: str, status_code: int) -> JsonResponse:
    """
    Retorna uma resposta HTTP com uma mensagem em formato JSON.

    Exemplo:

    ```json
    {
        "detail": :param: message
    }
    ```

    Se `status_code` for de erro, a mensagem segue o padrão:
    'Falha na solicitação.' + `message`

    Se `status_code` não for de erro, retorna:
    'Solicitação concluída com sucesso.' + `message`
    """
    type_message = 'Solicitação concluída com sucesso'

    if status_code >= status.HTTP_400_BAD_REQUEST:
        type_message = 'Falha na solicitação'

    return JsonResponse(
        {
            'detail': f'{type_message}. {message}'
        }, status=status_code
    )
