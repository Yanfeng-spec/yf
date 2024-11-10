from django.contrib import admin
from .models import Movie,Review
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title', 'description']
    list_editable = ('description',)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Review)