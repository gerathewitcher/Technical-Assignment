from django.contrib import admin
from .models import News

# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content',  'author', 'published']
    list_filter = ('id',)
    search_fields = ('title',)