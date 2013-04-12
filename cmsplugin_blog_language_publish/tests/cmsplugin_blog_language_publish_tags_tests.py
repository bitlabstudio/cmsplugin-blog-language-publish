"""Tests for the ``cmsplugin_blog_language_publish`` app's template tags."""
from django.test import TestCase

from ..templatetags.cmsplugin_blog_language_publish_tags import (
    get_published_entry)
from .factories import EntryLanguagePublishFactory


class GetPublishedEntryTestCase(TestCase):
    """Test for the ``get_published_entry`` template tag."""
    longMessage = True

    def setUp(self):
        self.entry_langpub = EntryLanguagePublishFactory(published=True)
        self.entry_not_published = EntryLanguagePublishFactory()

    def test_template_tag(self):
        """Test for the ``get_published_entry`` template tag."""
        entry = get_published_entry(self.entry_langpub.entry, 'en')
        self.assertEqual(entry, self.entry_langpub.entry, msg=(
            'When the correct language is published, the tag should return the'
            ' entry.'))

        entry = get_published_entry(self.entry_not_published.entry, 'en')
        self.assertIsNone(entry, msg=(
            'When the entry is not published in this language, it should'
            ' return None.'))
