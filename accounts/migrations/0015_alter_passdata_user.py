# Generated by Django 4.0 on 2022-11-16 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0014_alter_product_tags_passdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passdata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
