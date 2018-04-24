# Generated by Django 2.0.4 on 2018-04-24 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('amount_invested', models.FloatField(blank=True, default=0)),
                ('current_balance', models.FloatField(blank=True, default=0)),
                ('chart', models.TextField(default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CryptoInvestment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.FloatField(default=None)),
                ('quantity', models.FloatField(default=None, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('performance', models.FloatField(default=None, null=True)),
                ('chart', models.TextField(default=None, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Cryptocurrency')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OptionInvestment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.FloatField(default=None)),
                ('quantity', models.FloatField(default=None, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('performance', models.FloatField(default=None, null=True)),
                ('chart', models.TextField(default=None, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Option')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockInvestment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.FloatField(default=None)),
                ('quantity', models.FloatField(default=None, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('performance', models.FloatField(default=None, null=True)),
                ('chart', models.TextField(default=None, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Stock')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
