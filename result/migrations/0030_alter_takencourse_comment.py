# Generated by Django 3.2.23 on 2024-04-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0029_alter_takencourse_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takencourse',
            name='comment',
            field=models.CharField(blank=True, choices=[(' 22/04/24', ' 22/04/24'), ('* 22/04/24', '* 22/04/24')], max_length=200),
        ),
    ]
