# Generated by Django 2.1 on 2021-01-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='타입')),
                ('content_kr', models.TextField(verbose_name='내용(한글)')),
                ('content_en', models.TextField(verbose_name='내용(영어)')),
                ('crt_dt', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
            ],
        ),
    ]
