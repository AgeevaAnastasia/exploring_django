# Generated by Django 4.2.4 on 2023-08-23 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('public_date', models.DateField(auto_now=True)),
                ('category', models.CharField(max_length=100)),
                ('views', models.IntegerField(default=0)),
                ('ispublic', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.author')),
            ],
        ),
    ]
