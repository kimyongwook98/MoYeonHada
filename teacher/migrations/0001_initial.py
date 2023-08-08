# Generated by Django 4.2.3 on 2023-08-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('number', models.PositiveIntegerField()),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]