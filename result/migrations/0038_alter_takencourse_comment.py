# Generated by Django 3.2.23 on 2024-06-16 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0037_alter_takencourse_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takencourse',
            name='comment',
            field=models.CharField(blank=True, choices=[(' 16/06/24', ' 16/06/24'), ('* 16/06/24', '* 16/06/24')], max_length=200),
        ),
    ]
