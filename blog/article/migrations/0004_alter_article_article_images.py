# Generated by Django 3.2.5 on 2021-08-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_article_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_images',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Sekil elave edin'),
        ),
    ]