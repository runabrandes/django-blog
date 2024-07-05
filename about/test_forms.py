from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Runa',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")


    def test_name_field_is_not_valid(self):
        """ Test name field"""
        form = CollaborateForm({
            'name':'',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Name was not provided but the form is valid")


    def test_email_field_is_not_valid(self):
        """ Test email field"""
        form = CollaborateForm({
            'name': 'Runa',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Email was not provided, but the form is valid")


    def test_message_form_is_not_valid(self):
        """ Test message field"""
        form = CollaborateForm({
            'name': 'Runa',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Message was not provided but the form is valid")