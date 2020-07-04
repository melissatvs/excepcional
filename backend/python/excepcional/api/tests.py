from django.test import TestCase
from api.models import User, Environment, Application, Event


class EnvironmentTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.environment = Environment.objects.create(
            name='Ambiente Teste',
            description='Ambiente de teste xxx'
        )

    def test_should_return_attributes(self):
        fields = (
            'name',
            'description'
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Environment, field))

    def test_should_create_item(self):
        self.assertIsNotNone(self.environment)

    def test_should_assert_methods(self):
        self.assertEqual(str(self.environment), 'Ambiente Teste')


class UserTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create(
            name='Melissa',
            e_mail='email@teste.com',
            password='xxx'
        )

    def test_should_return_attributes(self):
        fields = (
            'name',
            'e_mail',
            'password',
            'date_created',
            'last_login'
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(User, field))

    def test_should_create_item(self):
        self.assertIsNotNone(self.user)

    def test_should_assert_methods(self):
        self.assertEqual(str(self.user), 'Melissa')


class ApplicationTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.application = Application.objects.create(
            name='Aplicativo de Comida',
            user=User.objects.create(
                name='Melissa',
                e_mail='email@teste.com',
                password='xxx'
            )
        )

        cls.environment = Environment.objects.create(
            name='Ambiente Teste',
            description='Ambiente de teste xxx'
        )
        cls.application.environment.add(cls.environment)

        cls.environment = Environment.objects.create(
            name='Ambiente Produção',
            description='Ambiente de produção xxx'
        )
        cls.application.environment.add(cls.environment)

    def test_should_return_attributes(self):
        fields = (
            'name',
            'environment',
            'user'
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Application, field))

    def test_should_create_item(self):
        self.assertIsNotNone(self.application)

    def test_should_assert_methods(self):
        self.assertEqual(str(self.application), 'Aplicativo de Comida')


class EventTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.application = Application.objects.create(
            name='Aplicativo de Comida',
            user=User.objects.create(
                name='Melissa',
                e_mail='email@teste.com',
                password='xxx'
            )
        )

        cls.environment = Environment.objects.create(
            name='Ambiente Teste',
            description='Ambiente de teste xxx'
        )
        cls.application.environment.add(cls.environment)

        cls.event = Event.objects.create(
            user_name='USUARIOX',
            level='E',
            ip_address='127.0.0.1',
            message='Mensagem de teste',
            application=cls.application,
            environment=cls.environment
        )

    def test_should_return_attributes(self):
        fields = (
            'datetime',
            'user_name',
            'level',
            'ip_address',
            'message',
            'application',
            'environment',
            'occurrences',
            'archived',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Event, field))

    def test_should_create_item(self):
        self.assertIsNotNone(self.event)

    def test_should_assert_methods(self):
        self.assertEqual(str(self.event), '127.0.0.1 E Mensagem de teste')
