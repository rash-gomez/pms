# Generated by Django 2.2 on 2019-06-04 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0003_auto_20190604_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drugs',
            name='name',
        ),
        migrations.AlterField(
            model_name='drugs',
            name='brand_name',
            field=models.CharField(help_text='brand name', max_length=100, verbose_name='Brand name'),
        ),
        migrations.AlterField(
            model_name='drugs',
            name='des',
            field=models.TextField(help_text='drug description', max_length=1000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='drugs',
            name='generic_name',
            field=models.CharField(help_text='scientific name', max_length=100, verbose_name='Generic name'),
        ),
    ]