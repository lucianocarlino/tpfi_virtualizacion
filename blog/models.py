from django.db import models

class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    legajo = models.CharField(max_length=20)
    carrera = models.CharField(max_length=100)
    email = models.EmailField()
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='profile/', blank=True, null=True)
    pdf_informe = models.FileField(upload_to='pdf/', blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

class LoginIntento(models.Model):
    usuario = models.CharField(max_length=150)
    exitoso = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Intento de login'
        verbose_name_plural = 'Intentos de login'

    def __str__(self):
        estado = 'exitoso' if self.exitoso else 'fallido'
        return f"{self.usuario} — {estado} — {self.timestamp}"