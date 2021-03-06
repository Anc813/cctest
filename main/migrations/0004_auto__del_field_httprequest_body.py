# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Deleting field 'HTTPRequest.body'
        db.delete_column(u'main_httprequest', 'body')


    def backwards(self, orm):
        # Adding field 'HTTPRequest.body'
        db.add_column(u'main_httprequest', 'body',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'unique': 'True', 'max_length': '80'}),
            'permissions': (
            'django.db.models.fields.related.ManyToManyField', [],
            {'to': u"orm['auth.Permission']", 'symmetrical': 'False',
             'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {
            'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')",
            'unique_together': "((u'content_type', u'codename'),)",
            'object_name': 'Permission'},
            'codename': (
            'django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [],
                             {'to': u"orm['contenttypes.ContentType']"}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': (
            'django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [],
                            {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [],
                      {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [],
                           {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'related_name': "u'user_set'",
                        'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': (
            'django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': (
            'django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': (
            'django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [],
                           {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [],
                          {'max_length': '30', 'blank': 'True'}),
            'password': (
            'django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': (
            'django.db.models.fields.related.ManyToManyField', [],
            {'symmetrical': 'False', 'related_name': "u'user_set'",
             'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [],
                         {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)",
                     'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType',
                     'db_table': "'django_content_type'"},
            'app_label': (
            'django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': (
            'django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': (
            'django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.httprequest': {
            'COOKIES': (
            'django.db.models.fields.TextField', [], {'null': 'True'}),
            'FILES': (
            'django.db.models.fields.TextField', [], {'null': 'True'}),
            'GET': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'META': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'Meta': {'ordering': "['-timestamp']",
                     'object_name': 'HTTPRequest'},
            'POST': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'encoding': ('django.db.models.fields.CharField', [],
                         {'max_length': '32', 'null': 'True'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': (
            'django.db.models.fields.CharField', [], {'max_length': '4'}),
            'path': ('django.db.models.fields.CharField', [],
                     {'max_length': '8192', 'null': 'True'}),
            'path_info': ('django.db.models.fields.CharField', [],
                          {'max_length': '8192', 'null': 'True'}),
            'session': (
            'django.db.models.fields.TextField', [], {'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [],
                          {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [],
                     {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'main.people': {
            'Meta': {'object_name': 'People'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': (
            'django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [],
                       {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'name': (
            'django.db.models.fields.CharField', [], {'max_length': '64'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [],
                      {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [],
                      {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'surname': (
            'django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['main']
