# Generated by Django 4.1.3 on 2022-12-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'dashboard_post',
            },
        ),
    ]
