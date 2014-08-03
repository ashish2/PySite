# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FBUserProfile'
        db.create_table('fb_fbuserprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fb_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(default=None, max_length=128, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('locale', self.gf('django.db.models.fields.CharField')(default=None, max_length=16, null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=1024)),
            ('imageurl', self.gf('django.db.models.fields.URLField')(max_length=2048)),
            ('timezone', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('accesstoken', self.gf('django.db.models.fields.CharField')(default=None, max_length=512, null=True, blank=True)),
            ('response', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('verified', self.gf('django.db.models.fields.NullBooleanField')(default=True, null=True, blank=True)),
        ))
        db.send_create_signal('fb', ['FBUserProfile'])


    def backwards(self, orm):
        # Deleting model 'FBUserProfile'
        db.delete_table('fb_fbuserprofile')


    models = {
        'fb.fbuserprofile': {
            'Meta': {'object_name': 'FBUserProfile'},
            'accesstoken': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fb_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageurl': ('django.db.models.fields.URLField', [], {'max_length': '2048'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '1024'}),
            'locale': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'verified': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fb']