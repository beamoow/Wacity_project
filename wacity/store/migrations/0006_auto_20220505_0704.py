# Generated by Django 3.2.3 on 2022-05-05 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_quantity_product_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='cart',
        ),
        migrations.AlterModelTable(
            name='purchase',
            table=None,
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]