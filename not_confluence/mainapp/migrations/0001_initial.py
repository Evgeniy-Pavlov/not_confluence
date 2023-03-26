# Generated by Django 4.1.7 on 2023-03-26 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=10, unique=True)),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20)),
                ('date_create', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('date_create', models.DateTimeField(null=True)),
                ('date_update', models.DateTimeField(blank=True, null=True)),
                ('user_create', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.user')),
                ('user_update', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_projects', to='mainapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('body', models.TextField(blank=True, max_length=3000, null=True)),
                ('date_create', models.DateTimeField(null=True)),
                ('date_update', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.user')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.project')),
                ('user_update', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_articles', to='mainapp.user')),
            ],
        ),
    ]