# Generated by Django 4.2.7 on 2023-11-29 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('starships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, verbose_name='Created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=8, verbose_name='Status')),
                ('sale_price', models.IntegerField(verbose_name='Asking Price')),
                ('sold', models.BooleanField(default=False, verbose_name='Sold')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Seller')),
                ('starship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='starships.starship', verbose_name='Starship')),
            ],
        ),
    ]
