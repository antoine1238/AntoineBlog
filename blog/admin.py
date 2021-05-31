from django.contrib import admin
from .models import *
from import_export import resources                    
from import_export.admin import ImportExportModelAdmin 


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria


class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor


class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["nombre"]
    list_display = ("nombre", "estado", "fecha_creacion")
    resource_class = CategoriaResource


class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_field = ["nombres", "apellidos"]
    list_display = ("nombres", "apellidos", "estado", "email", "fecha_creacion")
    list_filter = ("estado", "fecha_creacion")
    resource_class = AutorResource


class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_field = ["titulo", "autor"]
    list_display = ("titulo", "autor", "fecha_creacion", "categoria", "estado")
    
    resource_class = PostResource


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)