# Generated by Django 5.0.2 on 2024-02-27 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id_nota', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_nota', models.TextField(max_length=200)),
                ('conteudo_nota', models.TextField(max_length=5000)),
            ],
        ),
    ]
