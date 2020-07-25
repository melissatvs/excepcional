# :warning:Excepcional:warning:

![Linguagem](https://img.shields.io/github/languages/top/melissatvs/excepcional) ![GitHub language count](https://img.shields.io/github/languages/count/melissatvs/excepcional) [![Tempo no Projeto](https://wakatime.com/badge/github/melissatvs/excepcional.svg)](https://wakatime.com/badge/github/melissatvs/excepcional) ![GitHub contributors](https://img.shields.io/github/contributors/melissatvs/excepcional)


Solução dada ao projeto do Aceleradev de Python da Stone.

Requisitos do projeto: [Central de Erros](central-erros.md)


## Resumo :sunglasses: 

API Rest que disponibiliza end-points para uma central de erros.

Os *eventos* de uma aplicação só podem ser registrados pela própria aplicação que gerou o *evento*.

A consulta dos *eventos*, exclusão, arquivamento, gerenciamento de aplicações e ambientes serão feitos por usuários.


## Recursos da API :monocle_face:

### [Usuário (user)](/reference/user.md)

*`POST`* api/user/ :key:

*`GET`* api/user/{id} :closed_lock_with_key:

*`PUT`* api/user/{id} :closed_lock_with_key:

*`DELETE`* api/user/{id} :closed_lock_with_key:


### [Chave de acesso do Usuário (user_token)](/reference/user_token.md)

*`POST`* api/user_token/ :key:


### [Ambiente (environment)](/reference/environment.md)

*`POST`* api/environment/ :closed_lock_with_key:

*`GET`* api/environment/ :closed_lock_with_key:

*`GET`* api/environment/{id} :closed_lock_with_key:

*`PUT`* api/environment/{id} :closed_lock_with_key:

*`DELETE`* api/environment/{id} :closed_lock_with_key:


### [Aplicação (application)](/reference/application.md)

*`POST`* api/application/ :closed_lock_with_key: :key:

*`GET`* api/application/ :closed_lock_with_key:

*`GET`* api/application/{id} :closed_lock_with_key:

*`PUT`* api/application/{id} :closed_lock_with_key:

*`DELETE`* api/application/{id} :closed_lock_with_key:


### [Chave de acesso da Aplicação (application_token)](/reference/application_token.md)

*`POST`* api/application_token/ :closed_lock_with_key: :key:


### [Evento da Aplicação (event)](/reference/event.md)

*`POST`* api/event/ :closed_lock_with_key:

*`GET`* api/event/ :closed_lock_with_key:

*`GET`* api/event/{id} :closed_lock_with_key:

*`PUT`* api/event/{id} :closed_lock_with_key:

*`DELETE`* api/event/{id} :closed_lock_with_key:


## [Clonou](https://github.com/melissatvs/excepcional/archive/master.zip)? :nerd_face:

### Crie um ambiente virtual

Instale o virtualenv: `pip3 install virtualenv`

Crie o amnbiente: `virtualenv [nome do ambiente virtual] -p python3`

Ative o ambiente: `source [nome do ambiente virtual]/Scripts/activate`

Instale as dependências: `pip install -r requirements.txt`

Para desativar, use o comando: `deactivate`


### Crie suas *Secrets*

Crie um arquivo com o nome `.env`,  no caminho `/backend/python`.
Insira nele as chaves secretas `SECRET_KEY`, `SECRET_USER`, e `SECRET_APP`.

Exemplo:
```
[settings]
SECRET_KEY = 'sua chave super secreta principal'
SECRET_USER = 'sua chave super secreta para usuário'
SECRET_APP = 'sua chave super secreta para aplicação'
```