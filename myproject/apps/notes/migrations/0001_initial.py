# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Note'
        db.create_table(u'notes_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body_text', self.gf('django.db.models.fields.TextField')()),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'notes', ['Note'])


    def backwards(self, orm):
        # Deleting model 'Note'
        db.delete_table(u'notes_note')


    models = {
        u'notes.note': {
            'Meta': {'object_name': 'Note'},
            'body_text': ('django.db.models.fields.TextField', [], {}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['notes']