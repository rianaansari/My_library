# Generated by Django 3.2.7 on 2021-09-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20210925_0546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={},
        ),
        migrations.RenameField(
            model_name='bookinstance',
            old_name='borrower',
            new_name='reader',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='due_back',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='imprint',
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('W', 'Want to read'), ('R', 'Read'), ('C', 'Currantly reading')], max_length=1),
        ),
    ]
