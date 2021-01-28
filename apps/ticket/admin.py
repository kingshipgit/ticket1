from django.contrib import admin

from .models import Ticket, Comment


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_by', 'status')
    list_filter = ('status', 'created', 'created_by')
    search_fields = ('subject', 'body')
    raw_id_fields = ('created_by',)
    ordering = ('status',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('comment',)
