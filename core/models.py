from django.db import models

# Create your models here.

class DatosContacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(verbose_name='Nombre', max_length=30)
    apellido = models.CharField(verbose_name='Apellido', max_length=30)
    correo = models.EmailField(verbose_name='Correo', max_length=250)
    telefono = models.IntegerField(verbose_name='Teléfono')
    mensaje = models.CharField(verbose_name='Mensaje',max_length=100)
    
    class Meta:
        verbose_name = 'nombre'
        verbose_name_plural = 'nombres'
        ordering = ['id']
        
    def __str__(self) -> str:
        return self.id   
