# Generated by Django 5.1.5 on 2025-02-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=100, verbose_name='نام عکس')),
                ('image', models.ImageField(upload_to='homecarousel', verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'عکس صفحه اصلی',
                'verbose_name_plural': 'عکس های صفحه اصلی',
            },
        ),
    ]
