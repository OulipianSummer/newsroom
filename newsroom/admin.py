from django.contrib import admin
from .models import Article, Section, Author

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','section', 'body',)
    prepopulated_fields = {'slug': ('title',)}

class SectionAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name', )}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'title', 'bio')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Author, AuthorAdmin)