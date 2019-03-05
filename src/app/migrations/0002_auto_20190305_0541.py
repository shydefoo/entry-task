# Generated by Django 2.1.7 on 2019-03-05 05:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6fcf481c-a6c8-4454-ae94-3762d4fe8ccc'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1f772670-84cc-4849-b4d4-5102e4144fe2'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3f21db05-cade-4b32-b151-07952fef43dc'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(to='app.Category'),
        ),
    ]
