from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    
    list_display = ('id','first_name','last_name')
    list_filter = ('id','first_name','last_name')
    search_fields = ('first_name',)
    ordering = ('first_name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle','content','publication_date','category')
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('title',)