# Usuário (user)

## *`POST`* `api/user/` :key:

Cria um novo usuário e retorna um json com os dados enviados, e um *token* de acesso. Esse *token* é a chave que deve ser usada para acesso de outros recursos disponibilizados para o usuário.

### Exemplo de requisição

**`body`**
```json
{
    "name": "superusuario",
    "e_mail": "superusuario@app.com.br",
    "password": "senhasupersecreta"
}
```

### Respostas

- 201 - Created

    ```json
    {
        "id": 1,
        "name": "superusuario",
        "e_mail": "superusuario@app.com.br",
        "password": "senhasupersecreta",
        "date_created": "2020-07-20T00:48:16.815017Z",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX25hbWUiOiJzdXBlcnVzdWFyaW8iLCJ1c2VyX3Bhc3N3b3JkIjoic2VuaGFzdXBlcnNlY3JldGEifQ.QpVsTKjk4jUq8k7PLRVw8HxAH7UN6r38METxXyjxxC8"
    }
    ```

- 400 - Bad Request
    ```json
    {
        "detail": "Falha na solicitação. Não foi possível criar o usuário"
    }
    ```


## *`GET`* `api/user/{id}` :closed_lock_with_key:

Retorna os dados de um usuário pelo id

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

### Parâmetros

- **id** - obrigatório

### Respostas

- 200 - OK
    ```json
    {
        "id": 1,
        "name": "superusuario",
        "e_mail": "superusuario@app.com.br",
        "date_created": "2020-07-20T00:48:16.815017Z",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX25hbWUiOiJzdXBlcnVzdWFyaW8iLCJ1c2VyX3Bhc3N3b3JkIjoic2VuaGFzdXBlcnNlY3JldGEifQ.QpVsTKjk4jUq8k7PLRVw8HxAH7UN6r38METxXyjxxC8"
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

## *`PUT`* `api/user/{id}` :closed_lock_with_key:

Altera o usuário pelo id

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


### Parâmetros 

- **id** - obrigatório

### Exemplo de requisição

**`body`**
```json
{
    "name": "superusuario",
    "e_mail": "superusuario@app.com.br",
    "password": "senhamaissecreta"
}

```

### Respostas

- 200 - OK
    ```json
    {
        "id": 1,
        "name": "superusuario",
        "e_mail": "superusuario@app.com.br",
        "password": "senhamaissecreta",
        "date_created": "2020-07-20T00:48:16.815017Z",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX25hbWUiOiJzdXBlcnVzdWFyaW8iLCJ1c2VyX3Bhc3N3b3JkIjoic2VuaGFtYWlzc2VjcmV0YSJ9.V4mUaubiWFzLGSAZavEnmmk7jY7xxqHiNl7mrHGWxFE"
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

## *`DELETE`* `api/user/{id}` :closed_lock_with_key:

Exclui o usuário pelo id

### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)
