# Generated by Django 2.1.3 on 2018-12-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(choices=[('BACK_OFFICE', 'back_office'), ('SALES_MARKETING', 'sales_marketing'), ('FRONT_OFFICE', 'front_office'), ('HOUSE_KEEPING', 'house_keeping'), ('FITNESS', 'fitness'), ('FOOD_BEVERAGE', 'food_beverage'), ('FINANCE', 'finance')], max_length=30, unique=True),
        ),
    ]
