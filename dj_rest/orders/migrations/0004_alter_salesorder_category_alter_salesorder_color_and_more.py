# Generated by Django 4.2.4 on 2023-08-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_salesorder_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='category',
            field=models.CharField(default='No category', max_length=50),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='color',
            field=models.CharField(default='no color', max_length=100),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='description',
            field=models.CharField(default='No description', max_length=600),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='name',
            field=models.CharField(default='No name', max_length=255),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='size',
            field=models.CharField(default='no size', max_length=10),
        ),
    ]
