# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Query.picked_up_by_processor'
        db.alter_column(u'tracker_query', 'picked_up_by_processor', self.gf('django.db.models.fields.BooleanField')())

    def backwards(self, orm):

        # Changing field 'Query.picked_up_by_processor'
        db.alter_column(u'tracker_query', 'picked_up_by_processor', self.gf('django.db.models.fields.NullBooleanField')(null=True))

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
            'picked_up_by_processor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'query_type': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'raw_results': ('jsonfield.fields.JSONField', [], {}),
            'time_executed': ('django.db.models.fields.DateTimeField', [], {}),
            'was_success': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tracker']