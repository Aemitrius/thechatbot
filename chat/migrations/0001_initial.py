# Generated by Django 2.1.3 on 2018-12-04 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questionaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(default=1, null=True)),
                ('log', models.TextField(default='')),
                ('questionaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionaire.Questionaire')),
            ],
        ),
    ]
