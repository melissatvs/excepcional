# Chave de acesso da Aplicação (application_token)

## *`POST`* `api/application_token/` :closed_lock_with_key: :key:

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


### Exemplo de requisição

**`body`**
```json
{
    "application_id": 1,
    "user_id": 1
}
```

### Respostas

- 201 - Created
    ```json
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBsaWNhdGlvbl9pZCI6MSwidXNlcl9pZCI6MX0.dfW8ga3qUGhNCG_EecOdhNn4ZysJ79-pu55oav2LHAs"
    }
    ```

- 404 - Not Found
    ```json
    {
        "detail": "Not found."
    }
    ```

- 403 - Forbidden
    ```json
    {
        "detail": "Não foi informado token de acesso da aplicação"
    }
