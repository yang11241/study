from django.contrib import admin
from .models import TestClass
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['main_category']

admin.site.register(TestClass, CategoryAdmin)
