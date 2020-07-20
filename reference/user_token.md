# [:house:](../readme.md)

# Chave de acesso do Usuário (user_token)

## *`POST`* `api/user_token/` :key:

### Exemplo de requisição

**`body`**
```json
{
    "user_name": "superusuario",
    "user_password": "senhamaissecreta"
}
```

### Respostas

- 201 - Created
    ```json
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX25hbWUiOiJzdXBlcnVzdWFyaW8iLCJ1c2VyX3Bhc3N3b3JkIjoic2VuaGFtYWlzc2VjcmV0YSJ9.V4mUaubiWFzLGSAZavEnmmk7jY7xxqHiNl7mrHGWxFE"
    }
    ```

- 404 - Not Found
    ```json
    {
        "detail": "Not found."
    }
    ```
