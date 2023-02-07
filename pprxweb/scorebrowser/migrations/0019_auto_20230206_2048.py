# Generated by Django 3.2.16 on 2023-02-07 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scorebrowser', '0018_auto_20230206_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='CabinetModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SongLock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scorebrowser.cabinetmodel')),
                ('region', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scorebrowser.region')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorebrowser.song')),
                ('version', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scorebrowser.version')),
            ],
        ),
        migrations.DeleteModel(
            name='Cabinet',
        ),
    ]