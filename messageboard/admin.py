from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'date',)

admin.site.register(Message, MessageAdmin)
