"""Models for the ``cmsplugin_blog_language_publish`` app."""
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class EntryLanguagePublish(models.Model):
    """
    Holds the information about the published state of a certain language of
    an entry.

    :entry: FK to the actual entry.
    :language: The language that this state should be active for.
    :published: The published state of the entry and this language.

    """

    entry = models.ForeignKey(
        'cmsplugin_blog.Entry',
        verbose_name=_('Entry'),
        related_name='published_languages',
    )

    language = models.CharField(
        verbose_name=_('Language'),
        max_length=32,
        choices=settings.LANGUAGES,
    )

    published = models.BooleanField(
        verbose_name=_('Published'),
        default=False,
    )

    class Meta:
        unique_together = ('entry', 'language')
