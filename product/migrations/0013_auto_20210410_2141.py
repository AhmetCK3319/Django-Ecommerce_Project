# Generated by Django 3.1.7 on 2021-04-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]