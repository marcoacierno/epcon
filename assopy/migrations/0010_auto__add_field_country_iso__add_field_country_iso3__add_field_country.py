# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Country.iso'
        db.add_column('assopy_country', 'iso', self.gf('django.db.models.fields.CharField')(default='', max_length=2), keep_default=False)

        # Adding field 'Country.iso3'
        db.add_column('assopy_country', 'iso3', self.gf('django.db.models.fields.CharField')(max_length=3, null=True), keep_default=False)

        # Adding field 'Country.numcode'
        db.add_column('assopy_country', 'numcode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True), keep_default=False)

        # Adding field 'Country.printable_name'
        db.add_column('assopy_country', 'printable_name', self.gf('django.db.models.fields.CharField')(default='', max_length=128), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Country.iso'
        db.delete_column('assopy_country', 'iso')

        # Deleting field 'Country.iso3'
        db.delete_column('assopy_country', 'iso3')

        # Deleting field 'Country.numcode'
        db.delete_column('assopy_country', 'numcode')

        # Deleting field 'Country.printable_name'
        db.delete_column('assopy_country', 'printable_name')


    models = {
        'assopy.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'iso3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numcode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'printable_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'vat_company': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vat_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'assopy.user': {
            'Meta': {'object_name': 'User'},
            'assopy_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '22', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'assopy_user'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'assopy.useridentity': {
            'Meta': {'object_name': 'UserIdentity'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'display_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'phoneNumber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.User']"})
        },
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
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['assopy']
