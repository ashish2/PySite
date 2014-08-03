# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'FBUserProfile.full_name'
        db.delete_column('fb_fbuserprofile', 'full_name')

        # Adding field 'FBUserProfile.name'
        db.add_column('fb_fbuserprofile', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)


        # Changing field 'FBUserProfile.imageurl'
        db.alter_column('fb_fbuserprofile', 'imageurl', self.gf('django.db.models.fields.URLField')(max_length=2048, null=True))

        # Changing field 'FBUserProfile.link'
        db.alter_column('fb_fbuserprofile', 'link', self.gf('django.db.models.fields.URLField')(max_length=1024, null=True))

    def backwards(self, orm):
        # Adding field 'FBUserProfile.full_name'
        db.add_column('fb_fbuserprofile', 'full_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Deleting field 'FBUserProfile.name'
        db.delete_column('fb_fbuserprofile', 'name')


        # Changing field 'FBUserProfile.imageurl'
        db.alter_column('fb_fbuserprofile', 'imageurl', self.gf('django.db.models.fields.URLField')(default=None, max_length=2048))

        # Changing field 'FBUserProfile.link'
        db.alter_column('fb_fbuserprofile', 'link', self.gf('django.db.models.fields.URLField')(default=None, max_length=1024))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fb.fbuserprofile': {
            'Meta': {'object_name': 'FBUserProfile'},
            'accesstoken': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fb_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageurl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'verified': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fb']