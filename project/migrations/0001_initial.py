# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Proyecto'
        db.create_table(u'project_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_proyecto', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tiempo_Inicio', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('tiempo_fin', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('acumulado_proyecto', self.gf('django.db.models.fields.IntegerField')(default='0', null=True)),
        ))
        db.send_create_signal(u'project', ['Proyecto'])

        # Adding model 'Tarea'
        db.create_table(u'project_tarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_tarea', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tiempo_Inicio', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('tiempo_fin', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('acumulado_tarea', self.gf('django.db.models.fields.IntegerField')(default='0', null=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Proyecto'])),
        ))
        db.send_create_signal(u'project', ['Tarea'])


    def backwards(self, orm):
        # Deleting model 'Proyecto'
        db.delete_table(u'project_proyecto')

        # Deleting model 'Tarea'
        db.delete_table(u'project_tarea')


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