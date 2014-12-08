# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Questions.optright'
        db.alter_column('laughguru_questions', 'optright', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'Questions.optright'
        db.alter_column('laughguru_questions', 'optright', self.gf('django.db.models.fields.CharField')(max_length=45))

    models = {
        'laughguru.questions': {
            'Meta': {'object_name': 'Questions'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'opta': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '45'}),
            'optb': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '45', 'null': 'True'}),
            'optc': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '45', 'null': 'True'}),
            'optd': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '45', 'null': 'True'}),
            'optright': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'orderques': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '45'}),
            'question': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '45'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['laughguru.Subject']"})
        },
        'laughguru.subject': {
            'Meta': {'object_name': 'Subject'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True'})
        }
    }

    complete_apps = ['laughguru']