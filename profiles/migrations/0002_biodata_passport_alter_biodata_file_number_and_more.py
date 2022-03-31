# Generated by Django 4.0.3 on 2022-03-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='passport',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='file_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='employmentdetails',
            name='grade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employmentdetails',
            name='ippis_no',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='employmentdetails',
            name='step',
            field=models.IntegerField(),
        ),
    ]