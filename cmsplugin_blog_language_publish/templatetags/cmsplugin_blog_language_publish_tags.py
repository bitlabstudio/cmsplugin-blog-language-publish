"""Tempalte tags fot the ``cmsplugin_blog_language_publish`` app."""
from django import template
from django.core.exceptions import ObjectDoesNotExist


register = template.Library()


@register.assignment_tag
def get_published_entry(entry, language):
    try:
        entry.published_languages.get(
            language=language, published=True)
    except ObjectDoesNotExist:
        return None
    return entry
