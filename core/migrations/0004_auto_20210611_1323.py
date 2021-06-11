# Generated by Django 3.2.3 on 2021-06-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_paymenttransaction_wallet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pharmacy',
            old_name='address',
            new_name='health_safety_code',
        ),
        migrations.RenameField(
            model_name='pharmacy',
            old_name='name',
            new_name='location_address',
        ),
        migrations.RenameField(
            model_name='pharmacybranch',
            old_name='health_safety_code',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='pharmacybranch',
            old_name='location_address',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='pharmacybranch',
            name='about',
        ),
        migrations.RemoveField(
            model_name='pharmacybranch',
            name='city',
        ),
        migrations.RemoveField(
            model_name='pharmacybranch',
            name='country',
        ),
        migrations.RemoveField(
            model_name='pharmacybranch',
            name='district',
        ),
        migrations.RemoveField(
            model_name='pharmacybranch',
            name='license_operate',
        ),
        migrations.RemoveField(
            model_name='pharmacybranch',
            name='name_of_pharmacy',
        ),
        migrations.RemoveField(
            model_name='pharmacybranch',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='pharmacybranch',
            name='province',
        ),
        migrations.RemoveField(
            model_name='pharmacybranch',
            name='website',
        ),
        migrations.RemoveField(
            model_name='pharmacybranch',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='about',
            field=models.TextField(default='test', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='city',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='country',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='district',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='license_operate',
            field=models.FileField(default='test', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='name_of_pharmacy',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='phone_number',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='province',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='website',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='zip_code',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
