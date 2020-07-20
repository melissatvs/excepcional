# Aplicação (application)

## *`POST`* `api/application/` :closed_lock_with_key: :key:

Cria uma nova aplicação

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

### Exemplo de requisição

**`body`**
```json
{
    "name": "Super App",
    "environment": [
        1,
        2
    ],
    "user": 1
}
```

### Respostas

- 201 - Created
    ```json
    {
        "id": 3,
        "name": "Super App",
        "environment": [
            1,
            2
        ],
        "user": 1
    }
    ```

- 400 - Bad Request
    ```json
    {
        "detail": "Falha na solicitação. Não foi possível criar a aplicação"
    }
    ```

- 403 - Forbidden
    ```json
    {
        "detail": "Não foi informado token de acesso da aplicação"
    }

## *`GET`* `api/application/` :closed_lock_with_key:

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


## *`GET`* `api/application/{id}` :closed_lock_with_key:

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


## *`PUT`* `api/application/{id}` :closed_lock_with_key:

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


## *`DELETE`* `api/application/{id}` :closed_lock_with_key:

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)
