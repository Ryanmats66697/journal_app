# Generated by Django 5.1 on 2024-09-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoodEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(choices=[('Happy', 'Happy'), ('Neutral', 'Neutral'), ('Sad', 'Sad'), ('Stressed', 'Stressed'), ('Angry', 'Angry')], max_length=20)),
                ('factors', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]