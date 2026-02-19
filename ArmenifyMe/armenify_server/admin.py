from django.contrib import admin

from ArmenifyMe.armenify_server.models import UserChatHistory


@admin.register(UserChatHistory)
class UserChatHistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "updated_at")
    readonly_fields = ("user", "messages", "updated_at")
