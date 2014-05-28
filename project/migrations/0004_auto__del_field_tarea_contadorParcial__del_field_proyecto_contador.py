# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Tarea.contadorParcial'
        db.delete_column(u'project_tarea', 'contadorParcial')

        # Deleting field 'Proyecto.contador'
        db.delete_column(u'project_proyecto', 'contador')


    def backwards(self, orm):
        # Adding field 'Tarea.contadorParcial'
        db.add_column(u'project_tarea', 'contadorParcial',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'Proyecto.contador'
        db.add_column(u'project_proyecto', 'contador',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    models = {
        u'project.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'acumulado_proyecto': ('django.db.models.fields.IntegerField', [], {'default': "'0'", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tiempo_Inicio': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'tiempo_fin': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'project.tarea': {
            'Meta': {'object_name': 'Tarea'},
            'acumulado_tarea': ('django.db.models.fields.IntegerField', [], {'default': "'0'", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_tarea': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Proyecto']"}),
            'tiempo_Inicio': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'tiempo_fin': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        }
    }

    complete_apps = ['project']