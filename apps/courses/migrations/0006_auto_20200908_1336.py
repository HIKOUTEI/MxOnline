# Generated by Django 2.2 on 2020-09-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='notice',
            field=models.CharField(default='', max_length=300, verbose_name='课程公告'),
        ),
    ]