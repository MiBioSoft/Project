from django.test import TestCase

# Create your tests here.

from databasemodels.models import Keyword


class KeywordTests(TestCase):
    # Tests for the Keyword model
    def test_str(self):
        word = Keyword(word='testing')
        self.assertEquals(str(word), 'testing')
    
