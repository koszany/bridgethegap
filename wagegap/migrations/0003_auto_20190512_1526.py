# Generated by Django 2.2 on 2019-05-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagegap', '0002_auto_20190512_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='country',
        ),
        migrations.RemoveField(
            model_name='cost',
            name='spending',
        ),
        migrations.RemoveField(
            model_name='minwage',
            name='country',
        ),
        migrations.RemoveField(
            model_name='spending',
            name='category',
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Cost',
        ),
        migrations.DeleteModel(
            name='MinWage',
        ),
        migrations.DeleteModel(
            name='Spending',
        ),
    ]
