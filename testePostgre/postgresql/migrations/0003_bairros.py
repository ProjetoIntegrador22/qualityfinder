# Generated by Django 5.0.6 on 2024-05-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgresql', '0002_nome_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
    ]
