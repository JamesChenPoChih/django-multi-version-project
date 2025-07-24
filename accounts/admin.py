from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('email', 'unique_id', 'is_active', 'last_login_at')
    search_fields = ('email', 'unique_id')
    list_filter = ('is_active',)