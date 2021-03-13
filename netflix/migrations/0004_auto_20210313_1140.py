# Generated by Django 3.1.7 on 2021-03-13 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0003_auto_20210313_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='rate',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='netflix.rate'),
        ),
    ]
