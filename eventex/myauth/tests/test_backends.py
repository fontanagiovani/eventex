# coding: utf-8
from django.contrib.auth import get_user_model
from django.test import TestCase
from eventex.myauth.backends import EmailBackend


class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='giovani',
            email='fontanagiovani@gmail.com',
            password='123456'
        )
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        user = self.backend.authenticate(
            email='fontanagiovani@gmail.com',
            password='123456'
        )
        self.assertIsNotNone(user)

    def test_wrong_password(self):
        user = self.backend.authenticate(
            email='fontanagiovani@gmail.com',
            password='654321'
        )
        self.assertIsNone(user)

    def test_unknow_user(self):
        user = self.backend.authenticate(
            email='unknow@email.com',
            password='741852'
        )
        self.assertIsNone(user)


class MultipleEmailsTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='user1',
            email='fontanagiovani@gmail.com',
            password='123456'
        )

        UserModel.objects.create_user(
            username='user2',
            email='fontanagiovani@gmail.com',
            password='123456'
        )

        self.backend = EmailBackend()

    def test_multiple_emails(self):
        user = self.backend.authenticate(
            email='fontanagiovani@gmail.com',
            password='123456'
        )
        self.assertIsNone(user)


class FuncionalEmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='giovani',
            email='fontanagiovani@gmail.com',
            password='123456'
        )

    def test_login_with_email(self):
        result = self.client.login(
            email='fontanagiovani@gmail.com',
            password='123456'
        )
        self.assertTrue(result)

    def test_login_with_username(self):
        result = self.client.login(
            username='fontanagiovani@gmail.com',
            password='123456'
        )
        self.assertTrue(result)

    def test_get_user(self):
        backend = EmailBackend()
        self.assertIsNotNone(backend.get_user(1))