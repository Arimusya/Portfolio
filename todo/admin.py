# admin.py
from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title', 'important', 'created', 'datecompleted')
    list_filter = ('important', 'created')
    search_fields = ('title', 'memo')

admin.site.register(Todo, TodoAdmin)
