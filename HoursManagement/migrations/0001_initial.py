# Generated by Django 4.1.7 on 2023-02-24 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internalid', models.IntegerField(null=True, verbose_name='Cat serial number from the csv')),
                ('name', models.CharField(max_length=1000, null=True, verbose_name='Name of the cat')),
                ('breed', models.CharField(max_length=100, null=True, verbose_name='Breed of the cat')),
                ('birth', models.DateField(null=True, verbose_name='Birthdate of the cat')),
                ('gender', models.CharField(max_length=100, null=True, verbose_name='Gender of the cat')),
                ('fur', models.CharField(max_length=100, null=True, verbose_name='Fur code of the cat')),
                ('number', models.CharField(max_length=200, null=True, verbose_name='Identification number of the cat')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Titles of the cat')),
                ('father', models.CharField(max_length=200, null=True, verbose_name='Identification of the Father of the cat')),
                ('mother', models.CharField(max_length=200, null=True, verbose_name='Identification of the Mother of the cat')),
                ('site', models.CharField(max_length=20, null=True, verbose_name='Site from which the cat is from')),
                ('health', models.CharField(max_length=500, null=True, verbose_name='Health information about the cat')),
                ('fatherLink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fatherLink_cat', to='HoursManagement.hour')),
                ('motherLink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='motherLink_cat', to='HoursManagement.hour')),
            ],
        ),
    ]