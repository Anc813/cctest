# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'People'
        db.create_table(u'main_people', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name',
             self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('surname',
             self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email',
             self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber',
             self.gf('django.db.models.fields.EmailField')(max_length=75,
                                                           null=True,
                                                           blank=True)),
            ('skype',
             self.gf('django.db.models.fields.CharField')(max_length=32,
                                                          null=True,
                                                          blank=True)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'main', ['People'])


    def backwards(self, orm):
        # Deleting model 'People'
        db.delete_table(u'main_people')


    models = {
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
            'skype': ('django.db.models.fields.CharField', [],
                      {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'surname': (
            'django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['main']
