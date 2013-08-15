# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name='Giovani J. Fontana',
                               slug='giovani-j-fontana',
                               url='http://eventex-fontanagiovani.herokuapp.com',
                               description='De volta ao desenvolvimento de software!')

        self.speaker.save()

    def test_create(self):
        'Speaker instance should be saved.'
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        'Speaker string representation should be the name.'
        self.assertEqual(u'Giovani J. Fontana', unicode(self.speaker))


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Giovani J. Fontana',
            slug='giovani-j-fontana',
            url='http://eventex-fontanagiovani.herokuapp.com',
            description='De volta ao desenvolvimento de software!')

    def test_email(self):
        'Contact must have email.'
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind='E',
                                         value='fontanagiovani@gmail.com')
        self.assertEqual(1,contact.pk)

    def test_phone(self):
        'Contact must have phone.'
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind='P',
                                         value='65-12345678')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        'Contact must have fax.'
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind='F',
                                         value='65-12345678')

    def test_kind(self):
        'Contact kind should be limited to E, P or F.'
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)


    def test_unicode(self):
        'Contact string representation should be value.'
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind='F',
                                         value='65-12345678')
        self.assertEqual('65-12345678', unicode(contact))