# Generated by Django 3.2.3 on 2021-05-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_advatisement_advertisement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='batch_no',
            new_name='attention',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='buy_price',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='c_gst',
            new_name='composition',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='medical_typ',
            new_name='frequecy',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='in_stock_total',
            new_name='gross',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='qty_in_strip',
            new_name='instock',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='s_gst',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sell_price',
            new_name='reader_limit',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='shelf_no',
            new_name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='edited_on',
            field=models.DateTimeField(auto_now_add=True, default=-2345),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default='user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='strength',
            field=models.CharField(default='wer', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(default='erty', max_length=255),
            preserve_default=False,
        ),
    ]
