# Generated by Django 3.2.5 on 2021-08-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20210817_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_images',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='Sekil elave edin'),
        ),
    ]
