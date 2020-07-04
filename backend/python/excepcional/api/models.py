from django.db import models


class Environment(models.Model):
    """
    Classe Modelo para Ambiente
    """
    name = models.CharField('Nome', max_length=30)
    description = models.TextField('Descrição')

    class Meta():
        db_table = 'environment'

    def __str__(self):
        return self.name


class User(models.Model):
    """
    Classe Modelo para Usuário
    """
    name = models.CharField('Nome', max_length=100)
    e_mail = models.EmailField('E-mail')
    password = models.CharField('Senha', max_length=50)
    date_created = models.DateTimeField('Data Criação', auto_now=True)
    last_login = models.DateTimeField('Último Acesso', null=True)

    class Meta():
        db_table = 'user'

    def __str__(self):
        return self.name


class Application(models.Model):
    """
    Classe Modelo para Aplicação
    """
    name = models.CharField('Nome', max_length=70)
    environment = models.ManyToManyField(Environment)
    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING)

    class Meta():
        db_table = 'application'

    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Classe Modelo para Evento
    """
    ERROR = 'E'
    CRITICAL = 'C'
    WARNING = 'W'
    INFORMATION = 'I'
    DEBUG = 'D'

    LEVELS = (
        (ERROR, 'Erro'),
        (CRITICAL, 'Crítico'),
        (WARNING, 'Aviso'),
        (INFORMATION, 'Informativo'),
        (DEBUG, 'Modo Dev.'),
    )

    datetime = models.DateTimeField('Data/Hora', auto_now=True)
    user_name = models.CharField('Usuário', max_length=50, null=True)
    level = models.CharField('Nível', max_length=11, choices=LEVELS)

    ip_address = models.GenericIPAddressField(
        'Endereço IP',
        max_length=39,
        unpack_ipv4=True
    )

    message = models.TextField('Mensagem')

    application = models.ForeignKey(
        Application,
        on_delete=models.deletion.DO_NOTHING
    )

    environment = models.ForeignKey(
        Environment,
        on_delete=models.deletion.DO_NOTHING
    )

    archived = models.BooleanField('Arquivado', default=False)
    archived_datetime = models.DateTimeField(
        'Data/Hora Arquivado',
        auto_now=False,
        null=True
    )

    class Meta:
        db_table = 'event'

    def __str__(self):
        return f'{self.ip_address} {self.level} {self.message}'

    @property
    def occurrences(self):
        return Event.objects.filter(
            application=self.application,
            environment=self.environment,
            message=self.message,
        ).count()
