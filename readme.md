# Excepcional

Solução dada ao projeto do Aceleradev de Python da Stone

Requisitos do projeto: [Central de Erros](central-erros.md)

![Linguagem](https://img.shields.io/github/languages/top/melissatvs/excepcional) ![GitHub language count](https://img.shields.io/github/languages/count/melissatvs/excepcional) [![Tempo no Projeto](https://wakatime.com/badge/github/melissatvs/excepcional.svg)](https://wakatime.com/badge/github/melissatvs/excepcional) ![GitHub contributors](https://img.shields.io/github/contributors/melissatvs/excepcional)

## Resumo

API Rest que disponibiliza end-points para uma central de erros.

Os *eventos* de uma aplicação só pode ser registrados pela própria aplicação que gerou o *evento*.

A consulta dos *eventos*, exclusão, arquivamento, gerenciamento de aplicações, ambientes serão feitos por usuários.

## Recursos da API

### Usuário (user)

#### *`POST`* `api/user/` :key:

Cria um novo usuário e retorna um json com os dados enviados, e um *token* de acesso. Esse *token* é a chave que deve ser usada para acesso de outros recursos disponibilizados para o usuário.

##### Exemplo de requisição

**`body`**
```json
{
    "name": "superusuario",
    "e_mail": "superusuario@app.com.br",
    "password": "senhasupersecreta"
}
```

##### Respostas

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


#### *`GET`* `api/user/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

Retorna os dados de um usuário pelo id

##### Parâmetros

- **id** - obrigatório


##### Respostas

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

#### *`PUT`* `api/user/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

Altera o usuário pelo id

##### Parâmetros 

- **id** - obrigatório

##### Exemplo de requisição

**`body`**
```json
{
    "name": "superusuario",
    "e_mail": "superusuario@app.com.br",
    "password": "senhamaissecreta"
}

```

##### Respostas

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

#### *`DELETE`* `api/user/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

Exclui o usuário pelo id

### Chave de acesso do Usuário (user_token)

#### *`POST`* `api/user_token/` :key:

##### Exemplo de requisição

**`body`**
```json
{

}
```

##### Respostas

**`body`**
```json
{
    
}
```


### Ambiente (environment)

#### *`POST`* `api/environment/` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

##### Exemplo de requisição

**`body`**
```json
{
    "name": "Produção",
    "description": "Ambiente de produção"
}
```

##### Respostas

- 201 - Created
    **`body`**
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

#### *`GET`* `api/environment/` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


#### *`GET`* `api/environment/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


#### *`PUT`* `api/environment/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


#### *`DELETE`* `api/environment/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)



### Aplicação (application)

#### *`POST`* `api/application/` :closed_lock_with_key: :key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

##### Exemplo de requisição

**`body`**
```json
{

}
```

##### Respostas

**`body`**
```json
{
    
}
```

#### *`GET`* `api/application/` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


#### *`GET`* `api/application/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


#### *`PUT`* `api/application/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


#### *`DELETE`* `api/application/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

### Chave de acesso da Aplicação (application_token)

#### *`POST`* `api/application_token/` :key:

##### Exemplo de requisição

**`body`**
```json
{

}
```

##### Respostas

**`body`**
```json
{
    
}
```


### Evento da Aplicação (event)

#### *`POST`* `api/event/` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso da *aplicação* fornecida na [criação da aplicação](#aplicação-application) ou na [geração de token](#chave-de-acesso-da-aplicação-application_token)

##### Exemplo de requisição

**`body`**
```json
{

}
```

##### Respostas

**`body`**
```json
{
    
}
```

#### *`GET`* `api/event/` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


#### *`GET`* `api/event/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


#### *`PUT`* `api/event/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)


#### *`DELETE`* `api/event/{id}` :closed_lock_with_key:

##### Autenticação

Usar chave de acesso do *usuário* fornecida na [criação do usuário](#usuário-user) ou na [geração de token](#chave-de-acesso-do-usuário-user_token)

