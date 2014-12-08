# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table('laughguru_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=None, max_length=1024, null=True)),
        ))
        db.send_create_signal('laughguru', ['Subject'])

        # Adding model 'Questions'
        db.create_table('laughguru_questions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['laughguru.Subject'])),
            ('question', self.gf('django.db.models.fields.CharField')(default=None, max_length=45)),
            ('opta', self.gf('django.db.models.fields.CharField')(default=None, max_length=45)),
            ('optc', self.gf('django.db.models.fields.CharField')(default=None, max_length=45, null=True)),
            ('optb', self.gf('django.db.models.fields.CharField')(default=None, max_length=45, null=True)),
            ('optd', self.gf('django.db.models.fields.CharField')(default=None, max_length=45, null=True)),
            ('optright', self.gf('django.db.models.fields.CharField')(default=None, max_length=45)),
            ('orderques', self.gf('django.db.models.fields.CharField')(default=None, max_length=45)),
        ))
        db.send_create_signal('laughguru', ['Questions'])


    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table('laughguru_subject')

        # Deleting model 'Questions'
        db.delete_table('laughguru_questions')


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
            'optright': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '45'}),
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