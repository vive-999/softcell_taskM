# Generated by Django 4.0.2 on 2022-02-09 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Incident_number', models.IntegerField()),
                ('issue_subject', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('service_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='group.group')),
            ],
        ),
    ]
