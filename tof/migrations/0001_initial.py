# Generated by Django 4.2 on 2023-04-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=20)),
                ('value1', models.IntegerField(null=True)),
                ('value2', models.IntegerField(null=True)),
                ('value3', models.IntegerField(null=True)),
                ('value4', models.IntegerField(null=True)),
                ('value5', models.IntegerField(null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('breakAction', models.BooleanField()),
                ('override', models.BooleanField()),
                ('speed', models.FloatField(default=0.0)),
                ('zone_coord1', models.IntegerField(null=True)),
                ('zone_coord2', models.IntegerField(null=True)),
                ('zone', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LdrData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('value1', models.IntegerField(null=True)),
                ('value2', models.IntegerField(null=True)),
                ('value3', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TofData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('value1', models.IntegerField(null=True)),
                ('value2', models.IntegerField(null=True)),
                ('value3', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TofData1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('value1', models.IntegerField(null=True)),
                ('value2', models.IntegerField(null=True)),
                ('value3', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TofData2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('value1', models.IntegerField(null=True)),
                ('value2', models.IntegerField(null=True)),
                ('value3', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VizData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('value1', models.IntegerField(null=True)),
                ('value2', models.IntegerField(null=True)),
                ('value3', models.IntegerField(null=True)),
            ],
        ),
    ]
