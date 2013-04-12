"""Admin classes for the ``cmsplugin_blog_language_publish`` app."""
from django.contrib import admin

from cmsplugin_blog.admin import EntryAdmin

from .models import EntryLanguagePublish


class EntryLanguagePublishInline(admin.TabularInline):
    model = EntryLanguagePublish
    extra = 1


EntryAdmin.inlines = EntryAdmin.inlines[:] + [EntryLanguagePublishInline]
