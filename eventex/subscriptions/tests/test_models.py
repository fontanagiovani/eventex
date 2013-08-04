#coding: utf-8
from datetime import datetime
from django.db import IntegrityError
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Giovani Jose Fontana',
            cpf='012345678901',
            email='fontanagiovani@gmail.com',
            phone='65-98765432'
        )

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u"Giovani Jose Fontana", unicode(self.obj))

    def test_paid_default_value_is_False(self):
        'By default paid must be False.'
        self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
            name='Giovani José Fontana',
            cpf='12345678901',
            email='fontanagiovani@gmail.com',
            phone='65-98765432'
        )

    def test_cpf_unique(self):
        'CPF must be unique.'
        s = Subscription(
            name='Giovani José Fontana',
            cpf='12345678901',
            email='giovani@gmail.com',
            phone='65-98765432'
        )
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email must be unique.'
        s = Subscription(
            name='Giovani José Fontana',
            cpf='12345678902',
            email='fontanagiovani@gmail.com',
            phone='65-98765432'
        )
        self.assertRaises(IntegrityError, s.save)