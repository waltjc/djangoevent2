# Generated by Django 4.0.1 on 2022-01-27 18:43

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='images',
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=stdimage.models.StdImageField(default=1, upload_to='produtos', verbose_name='Imagem'),
            preserve_default=False,
        ),
    ]