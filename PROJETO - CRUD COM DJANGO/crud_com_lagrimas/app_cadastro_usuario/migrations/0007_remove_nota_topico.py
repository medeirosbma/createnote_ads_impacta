# Generated by Django 5.0.2 on 2024-04-23 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuario', '0006_alter_nota_topico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='topico',
        ),
    ]
