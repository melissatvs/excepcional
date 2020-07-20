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

#### *`POST`* `api/user/`

Cria um novo usuário e retorna um json com os dados enviados, e um *token* de acesso. Esse *token* é a chave que deve ser usada para acesso de outros recursos disponibilizados para o usuário.

**Exemplo de requisição**

**`body`**
```json
{
    "name": "superusuario",
    "e_mail": "superusuario@app.com.br",
    "password": "senhasupersecreta"
}
```

**Respostas**

- 201 - Usuário criado
    **`body`**
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
    **`body`**
    ```json
    {
        "detail": "Falha na solicitação. Não foi possível criar o usuário"
    }
    ```


#### *`GET`* `api/user/{id}`




#### *`POST`* `api/user/{id}`

**Exemplo de requisição**

**`body`**
```json
{

}
```

**Respostas**

**`body`**
```json
{
    
}
```

#### *`DELETE`* `api/user/{id}`



### Chave de acesso do Usuário (user_token)

#### *`POST`* `api/user_token/`

**Exemplo de requisição**

**`body`**
```json
{

}
```

**Respostas**

**`body`**
```json
{
    
}
```


### Ambiente (environment)

#### *`POST`* `api/environment/`

**Exemplo de requisição**

**`body`**
```json
{
    "name": "Produção",
    "description": "Ambiente de produção"
}
```

**Respostas**

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

#### *`GET`* `api/environment/`


#### *`GET`* `api/environment/{id}`


#### *`PUT`* `api/environment/{id}`


#### *`DELETE`* `api/environment/{id}`



### Aplicação (application)

#### *`POST`* `api/application/`

**Exemplo de requisição**

**`body`**
```json
{

}
```

**Respostas**

**`body`**
```json
{
    
}
```

#### *`GET`* `api/application/`


#### *`GET`* `api/application/{id}`


#### *`PUT`* `api/application/{id}`


#### *`DELETE`* `api/application/{id}`

### Chave de acesso da Aplicação (application_token)

#### *`POST`* `api/application_token/`

**Exemplo de requisição**

**`body`**
```json
{

}
```

**Respostas**

**`body`**
```json
{
    
}
```


### Evento da Aplicação (event)

#### *`POST`* `api/event/`

**Exemplo de requisição**

**`body`**
```json
{

}
```

**Respostas**

**`body`**
```json
{
    
}
```

#### *`GET`* `api/event/`


#### *`GET`* `api/event/{id}`


#### *`PUT`* `api/event/{id}`


#### *`DELETE`* `api/event/{id}`

