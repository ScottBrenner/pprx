# Generated by Django 3.2.16 on 2023-10-07 21:51

from django.db import migrations, models
import django.db.models.deletion

def forward(apps, schema_editor):
    UserChartBookmarks = apps.get_model("scorebrowser", "UserChartBookmarks")
    UserChartNotes = apps.get_model("scorebrowser", "UserChartNotes")
    UserChartAux = apps.get_model("scorebrowser", "UserChartAux")
    
    aux_created = {}
    for note in UserChartNotes.objects.all():
        new_aux = UserChartAux.objects.create(user_id=note.user_id, chart_id=note.chart_id, notes=note.notes)
        aux_created[(new_aux.user_id, new_aux.chart_id)] = new_aux

    for bookmark in UserChartBookmarks.objects.all():
        if (bookmark.user_id, bookmark.chart_id) in aux_created:
            aux = aux_created[(bookmark.user_ud, bookmark.chart_id)]
            aux.bookmark = True
            aux.save()
        else:
            UserChartAux.objects.create(user_id=bookmark.user_id, chart_id=bookmark.chart_id, bookmark=True)


def backward(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('scorebrowser', '0084_userchartbookmarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserChartAux',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bookmark', models.BooleanField(default=False)),
                ('notes', models.TextField(default='')),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorebrowser.chart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorebrowser.user')),
            ],
        ),

        migrations.RunPython(forward, backward),

        migrations.RemoveField(
            model_name='userchartnotes',
            name='chart',
        ),
        migrations.RemoveField(
            model_name='userchartnotes',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserChartBookmarks',
        ),
        migrations.DeleteModel(
            name='UserChartNotes',
        ),
    ]