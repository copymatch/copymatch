# Generated by Django 5.1.1 on 2024-10-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_remove_profilecl_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122, null=True)),
                ('feedback', models.TextField()),
            ],
        ),
    ]