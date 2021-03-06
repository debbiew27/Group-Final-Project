# Generated by Django 3.1.5 on 2022-04-19 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icebreaker', '0002_auto_20220418_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('userhash', models.CharField(max_length=50)),
                ('answer', models.TextField()),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='icebreaker.question')),
            ],
        ),
    ]
