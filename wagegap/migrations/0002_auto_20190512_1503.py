# Generated by Django 2.2 on 2019-05-12 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagegap', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minwage',
            name='id',
        ),
        migrations.RemoveField(
            model_name='spending',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='minwage',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='wagegap.Country'),
        ),
        migrations.AlterField(
            model_name='spending',
            name='name',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
