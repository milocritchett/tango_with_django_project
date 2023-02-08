from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields':['title']}),
	('category', {'fields':['category']}),
	('URL', {'fields':['url']})
	]
	list_display = ('title', 'category', 'url')
	
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)