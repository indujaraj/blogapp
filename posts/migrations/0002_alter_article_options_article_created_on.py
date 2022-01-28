# Generated by Django 4.0.1 on 2022-01-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='article',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
