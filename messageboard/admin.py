from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    fields = ['author', 'message']
    readonly_field = ('date',)
    list_display = ('author', 'date')

admin.site.register(Message, MessageAdmin)
