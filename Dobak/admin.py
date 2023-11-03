from django.contrib import admin

from .models import Match, Choice

# Register your models here.

admin.site.register(Match)
admin.site.register(Choice)