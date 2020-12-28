# Generated by Django 3.1.1 on 2020-12-27 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='diningHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmd.school')),
            ],
        ),
        migrations.CreateModel(
            name='diningHallReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diningHall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmd.dininghall')),
            ],
        ),
        migrations.AddField(
            model_name='dininghall',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmd.school'),
        ),
    ]
