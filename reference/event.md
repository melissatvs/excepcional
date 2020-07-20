# Evento da Aplicação (event)

## *`POST`* `api/event/` :closed_lock_with_key:

### Autenticação

Usar chave de acesso da *aplicação* fornecida na [criação da aplicação](#aplicação-application) ou na [geração de token](#chave-de-acesso-da-aplicação-application_token)

### Exemplo de requisição

**`body`**
```json
{
    "user_name": "USER_VILAO",
    "level": "E",
    "ip_address": "128.0.0.1",
    "message": "Access Violation, que é o erro que mais ocorre com programadores delphi jr.",
    "application": 1,
    "environment": 1
}
```

### Respostas

- 201 - Created
    ```json
    {
        "id": 1,
        "datetime": "2020-07-20T02:16:41.889854Z",
        "user_name": "USER_VILAO",
        "level": "E",
        "ip_address": "128.0.0.1",
        "message": "Access Violation, que é o erro que mais ocorre com programadores delphi jr.",
        "application": 1,
        "environment": 1,
        "occurrences": 1
    }
    ```

- 400 - Bad Request
    ```json
    {
        "detail": "Falha na solicitação. Não foi possível inserir o evento!"
    }
    ```

- 403 - Forbidden
    ```json
    {
        "detail": "Não foi informado token de acesso da aplicação"
    }

## *`GET`* `api/event/` :closed_lock_with_key:

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


## *`GET`* `api/event/{id}` :closed_lock_with_key:

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

## *`PUT`* `api/event/{id}` :closed_lock_with_key:

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


## *`DELETE`* `api/event/{id}` :closed_lock_with_key:

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

