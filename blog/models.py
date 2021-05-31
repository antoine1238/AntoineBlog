from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField("Nombre", max_length = 100, null = False, blank = False)
    estado = models.BooleanField("Activo/Inactivo", default = True)
    fecha_creacion = models.DateField("Fecha de creación", auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField("Nombres", max_length = 100, null = False, blank = False)
    apellidos = models.CharField("Apellidos", max_length = 100, null = False, blank = False)
    email = models.EmailField("Email", null = False, blank = False)
    estado = models.BooleanField("Activo/Inactivo", default = True)
    web = models.URLField("Web", null = True, blank = True)   
    twiter = models.URLField("Twiter", null = True, blank = True)   
    facebook = models.URLField("Facebook", null = True, blank = True)   
    instagram = models.URLField("Instagram", null = True, blank = True)   
    fecha_creacion = models.DateField("Fecha de creación", auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"{self.apellidos} {self.nombres}"


class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField("Título", max_length = 100, blank = False, null = False)
    slug = models.CharField("Slug", max_length = 100, blank = False, null = False)
    descripcion = models.CharField("Descripción", max_length = 100, blank = False, null = False)
    contenido = RichTextField()
    imagen = models.URLField(max_length = 255, blank = False, null = False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField("Activo/Inactivo", default = True)
    fecha_creacion = models.DateField("Fecha de creación", auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo