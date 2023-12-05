# Generated by Django 5.0 on 2023-12-05 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteerapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('content', models.CharField(max_length=3000)),
                ('address', models.CharField(max_length=3000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteerapi.volunteerusers')),
            ],
        ),
        migrations.CreateModel(
            name='InterestVolunteers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteerapi.volunteerusers')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteerapi.jobposts')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteerapi.volunteerusers')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteerapi.jobposts')),
            ],
        ),
        migrations.AddField(
            model_name='volunteerusers',
            name='favorite',
            field=models.ManyToManyField(related_name='volunteer', through='volunteerapi.Favorites', to='volunteerapi.jobposts'),
        ),
        migrations.CreateModel(
            name='PostCause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteerapi.causeareas')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteerapi.jobposts')),
            ],
        ),
        migrations.CreateModel(
            name='UserCause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteerapi.causeareas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteerapi.volunteerusers')),
            ],
        ),
        migrations.AddField(
            model_name='volunteerusers',
            name='cause_area',
            field=models.ManyToManyField(related_name='user', through='volunteerapi.UserCause', to='volunteerapi.causeareas'),
        ),
    ]
