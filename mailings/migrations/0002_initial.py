# Generated by Django 5.1.1 on 2024-10-24 07:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mailings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='чей клиент'),
        ),
        migrations.AddField(
            model_name='notification',
            name='client',
            field=models.ManyToManyField(related_name='clients', to='mailings.client', verbose_name='клиент'),
        ),
        migrations.AddField(
            model_name='notification',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.message', verbose_name='сообщение'),
        ),
        migrations.AddField(
            model_name='notificationattempt',
            name='notification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.notification', verbose_name='рассылка'),
        ),
    ]
