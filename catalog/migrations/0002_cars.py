# Generated by Django 3.1.3 on 2020-11-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='car name', max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('date_on', models.DateField()),
                ('date_off', models.DateField()),
            ],
        ),
    ]
