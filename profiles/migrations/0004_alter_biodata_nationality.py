# Generated by Django 4.0.3 on 2022-04-14 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_biodata_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='nationality',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.country'),
        ),
    ]
