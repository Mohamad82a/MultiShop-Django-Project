# Generated by Django 5.1.5 on 2025-02-02 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spectaculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec', to='product.product')),
            ],
        ),
    ]
