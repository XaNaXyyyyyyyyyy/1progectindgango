from django.contrib import admin
from .models import Author, Book, Genre, Language, Publisher, Status, BookInstance
from django.utils.html import format_html

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ('last_name', 'first_name', ('date_of_birth', 'photo'))
    readonly_fields = ["show_photo"]
    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 100px">')
    show_photo.short_description = 'Фото'

admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]
    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style ="max-hieght:100px">')
    show_photo.short_description = 'Обложка'

@admin.register(BookInstance)
class BookiInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id') 
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'inv_nom')}),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back', 'borrower')})
    )

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)