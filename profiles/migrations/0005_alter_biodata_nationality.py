# Generated by Django 4.0.3 on 2022-04-14 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_biodata_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='nationality',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='profiles.country'),
        ),
    ]
