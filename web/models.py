from django.db import models

# Create your models here.
class Contacto(models.Model):

    ORIGEN = (
        (1, 'Malla'),
        (2, 'Información'),
    )

    # atributos (generales)
    origen = models.IntegerField(choices=ORIGEN, blank=True, null=True)

    # atributos (generales) Ficha Personal
    nombre                = models.CharField(max_length=100)
    correo                = models.EmailField()
    telefono              = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        verbose_name        = 'Contacto'
        verbose_name_plural = 'Contactos'
