# Ambiente (environment)

## *`POST`* `api/environment/` :closed_lock_with_key:

Cria um novo ambiente

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

### Exemplo de requisição

**`body`**
```json
{
    "name": "Produção",
    "description": "Ambiente de produção"
}
```

### Respostas

- 201 - Created
    ```json
    {
        "id": 4,
        "name": "Produção",
        "description": "Ambiente de produção"
    }
    ```

- 400 - Bad Request
    ```json
    {
        "detail": "Falha na solicitação. Não foi possível criar o ambiente"
    }
    ```

- 403 - Forbidden
    ```json
    {
        "detail": "Não foi informado token de acesso da aplicação"
    }

## *`GET`* `api/environment/` :closed_lock_with_key:

Retorna uma lista com todos ambientes

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


## *`GET`* `api/environment/{id}` :closed_lock_with_key:

Busca o ambiente pelo id

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


## *`PUT`* `api/environment/{id}` :closed_lock_with_key:

Altera os dados do ambiente pelo id

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


## *`DELETE`* `api/environment/{id}` :closed_lock_with_key:

Exclui o ambiente pelo id

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)
