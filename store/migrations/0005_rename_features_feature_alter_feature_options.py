# Generated by Django 5.1.7 on 2025-03-31 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_feature_features_alter_features_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Features',
            new_name='Feature',
        ),
        migrations.AlterModelOptions(
            name='feature',
            options={'verbose_name': 'Feature', 'verbose_name_plural': 'Features'},
        ),
    ]
