# Generated by Django 3.1 on 2020-08-27 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=4, max_digits=10)),
                ('currency_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='currency.currency')),
                ('currency_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='currency.currency')),
            ],
        ),
    ]