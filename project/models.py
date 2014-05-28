from django.db import models

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=200)
    tiempo_Inicio = models.DateTimeField('Inicio Proyecto', null=True)
    tiempo_fin = models.DateTimeField('Fin Proyecto', null=True)
    acumulado_proyecto = models.IntegerField('acumulado Proyecto', null=True, default='0')
    def __str__(self):  
        return self.nombre_proyecto

    class Meta:
        permissions = (
            # Permission identifier     human-readable permission name
            ("crear_proyecto",               "Puede crear un proyecto"),
            ("crear_tarea",                "Puede crear una tarea"),
            ("empezar_tarea",               "Puede dar inicio a una tarea"),
        )
        
class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=200)
    tiempo_Inicio = models.DateTimeField('Inicio Tarea', null=True)
    tiempo_fin = models.DateTimeField('Fin Tarea', null=True)
    acumulado_tarea = models.IntegerField('acumulado Tarea', null=True, default='0')
    proyecto = models.ForeignKey(Proyecto)
    def __str__(self):  
        return self.nombre_tarea
