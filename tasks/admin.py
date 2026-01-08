"""
Admin configuration for tasks application.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Task, UserProfile


class UserProfileInline(admin.StackedInline):
    """Inline admin for user profile."""
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    """Extended user admin."""
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin configuration for Task model."""
    
    list_display = (
        'title',
        'user',
        'priority',
        'status',
        'due_date',
        'created_at',
        'is_overdue'
    )
    list_filter = ('status', 'priority', 'created_at', 'due_date')
    search_fields = ('title', 'description', 'user__username')
    readonly_fields = ('created_at', 'updated_at', 'completed_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'title', 'description')
        }),
        ('Task Details', {
            'fields': ('priority', 'status', 'due_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'completed_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_completed', 'mark_as_pending', 'set_high_priority']
    
    def mark_as_completed(self, request, queryset):
        """Bulk action to mark tasks as completed."""
        updated = queryset.update(status='completed')
        self.message_user(request, f'{updated} task(s) marked as completed.')
    mark_as_completed.short_description = "Mark selected tasks as completed"
    
    def mark_as_pending(self, request, queryset):
        """Bulk action to mark tasks as pending."""
        updated = queryset.update(status='pending')
        self.message_user(request, f'{updated} task(s) marked as pending.')
    mark_as_pending.short_description = "Mark selected tasks as pending"
    
    def set_high_priority(self, request, queryset):
        """Bulk action to set high priority."""
        updated = queryset.update(priority='high')
        self.message_user(request, f'{updated} task(s) set to high priority.')
    set_high_priority.short_description = "Set high priority for selected tasks"


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin configuration for UserProfile model."""
    
    list_display = ('user', 'phone_number', 'birth_date', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
