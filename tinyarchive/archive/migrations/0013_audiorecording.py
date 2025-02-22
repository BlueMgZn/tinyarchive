# Generated by Django 4.0.5 on 2023-07-26 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0012_alter_artifact_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioRecording',
            fields=[
                ('archivedocument_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='archive.archivedocument')),
                ('language', models.CharField(max_length=200)),
                ('speaker', models.CharField(max_length=200)),
                ('recording_date', models.DateField(auto_now=True)),
                ('audio_file', models.FileField(null=True, upload_to='sounds/')),
            ],
            bases=('archive.archivedocument',),
        ),
    ]
