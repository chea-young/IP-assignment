from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [ (None, {'fields':['headline']}),
    ('Data information', {'fields':['content','pub_date','reporter',]}), ]
    list_display = ('headline', 'pub_date')
    search_fields = ['content']

admin.site.register(models.Reporter)
admin.site.register(models.Article, ArticleAdmin)