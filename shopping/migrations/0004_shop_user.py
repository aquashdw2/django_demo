# Generated by Django 3.2.8 on 2021-10-27 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_info_shop'),
        ('shopping', '0003_alter_itemimages_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owning_shop', to='accounts.info'),
        ),
    ]
