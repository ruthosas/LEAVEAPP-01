# Generated by Django 4.0.3 on 2022-05-24 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registry', '0009_remove_department_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_head_of_sub_unit', models.BooleanField(default=False)),
                ('is_head_of_unit', models.BooleanField(default=False)),
                ('is_head_of_dept', models.BooleanField(default=False)),
                ('is_head_of_directorate', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
