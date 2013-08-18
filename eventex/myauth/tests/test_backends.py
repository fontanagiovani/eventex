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
            email='fontanagiovani',
            password='123456'
        )
        self.assertIsNotNone(user)