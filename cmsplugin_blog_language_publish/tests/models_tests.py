"""Tests for the models of the ``cmsplugin_blog_language_publish`` app."""
from django.test import TestCase

from cmsplugin_blog.models import Entry

from ..models import EntryLanguagePublish
from .factories import EntryLanguagePublishFactory


class EntryLanguagePublishTestCase(TestCase):
    """Tests for the ``EntryLanguagePublish`` model class."""
    longMessage = True

    def test_instantiation(self):
        """
        Test instantiation and save of the ``EntryLanguagePublish`` model.

        """
        EntryLanguagePublishFactory()
        self.assertEqual(EntryLanguagePublish.objects.all().count(), 1, msg=(
            'There should be one EntryLanguagePublish object.'))
        self.assertEqual(Entry.objects.all().count(), 1, msg=(
            'There should be one Entry object.'))
