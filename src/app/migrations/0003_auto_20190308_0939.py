# Generated by Django 2.1.7 on 2019-03-08 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190308_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9b14041f-65d0-4125-97f7-60e0a14bcbe9'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.UUIDField(default=uuid.UUID('06861362-8d92-4586-a849-fa09b5a3a4fa'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3189ca26-d83b-4fda-a3b6-f34c0fb97e16'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usersalttable',
            name='salt',
            field=models.UUIDField(default=uuid.UUID('675465ea-481c-474a-9d1b-97723661dfd6')),
        ),
    ]