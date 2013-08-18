# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker, Contact, Talk


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Givoani J. Fontana',
            slug='giovani-j-fontana',
            url='http://eventex-fontanagiovani.herokuapp.com')

        s.contact_set.add(Contact(kind='E', value='fontanagiovani@gmail.com'),
                          Contact(kind='P', value='65-12345678'),
                          Contact(kind='F', value='65-87654321'))

    def test_emails(self):
        qs = Contact.emails.all()
        expected = ['<Contact: fontanagiovani@gmail.com>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        qs = Contact.phones.all()
        expected = ['<Contact: 65-12345678>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        qs = Contact.faxes.all()
        expected = ['<Contact: 65-87654321>']
        self.assertQuerysetEqual(qs, expected)


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start_time='10:00')
        Talk.objects.create(title='Afternoon Talk', start_time='12:00')

    def test_morning(self):
        'Should return only tasks before 12:00'
        self.assertQuerysetEqual(
            Talk.objects.at_morning(), ['Morning Talk'],
            lambda t: t.title)

    def test_morning(self):
        'Should return only tasks after 11:59:59'
        self.assertQuerysetEqual(
            Talk.objects.at_afternoon(), ['Afternoon Talk'],
            lambda t: t.title)