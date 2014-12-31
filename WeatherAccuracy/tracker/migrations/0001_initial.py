# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'tracker_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('city_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'tracker', ['City'])

        # Adding model 'Query'
        db.create_table(u'tracker_query', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracker.City'])),
            ('time_executed', self.gf('django.db.models.fields.DateTimeField')()),
            ('query_type', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('full_query_string', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('raw_results', self.gf('jsonfield.fields.JSONField')()),
            ('was_success', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'tracker', ['Query'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'tracker_city')

        # Deleting model 'Query'
        db.delete_table(u'tracker_query')


    models = {
        u'tracker.city': {
            'Meta': {'ordering': "('name',)", 'object_name': 'City'},
            'city_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'tracker.query': {
            'Meta': {'ordering': "('-time_executed', 'city')", 'object_name': 'Query'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.City']"}),
            'full_query_string': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query_type': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'raw_results': ('jsonfield.fields.JSONField', [], {}),
            'time_executed': ('django.db.models.fields.DateTimeField', [], {}),
            'was_success': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tracker']