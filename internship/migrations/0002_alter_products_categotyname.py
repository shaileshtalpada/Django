# Generated by Django 4.0.5 on 2022-06-23 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='categotyname',
            field=models.ForeignKey(db_column='categoryname', default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='internship.category'),
        ),
    ]
