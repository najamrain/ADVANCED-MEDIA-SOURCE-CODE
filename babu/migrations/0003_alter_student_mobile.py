# Generated by Django 3.2.5 on 2022-01-29 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babu', '0002_alter_student_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(max_length=8),
        ),
    ]
