# Generated by Django 5.1.1 on 2024-10-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='превью'),
        ),
    ]