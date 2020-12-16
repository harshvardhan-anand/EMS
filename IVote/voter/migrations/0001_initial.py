# Generated by Django 3.1.3 on 2020-12-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_start', models.DateField(auto_now_add=True)),
                ('election_end', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('poll_started', models.BooleanField(default=False)),
                ('result_declared', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-election_start',),
            },
        ),
    ]