# Generated by Django 4.0 on 2021-12-24 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blango_auth', '0001_initial'),
        ('Blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blango_auth.user'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blango_auth.user'),
        ),
    ]
