# Generated by Django 4.2.3 on 2023-08-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneday', '0005_alter_onedayapply_memo_alter_onedaycreate_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onedaycreate',
            name='status',
        ),
    ]