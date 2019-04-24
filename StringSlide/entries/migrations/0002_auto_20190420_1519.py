# Generated by Django 2.2 on 2019-04-20 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('guitar_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('manufacturer_name', models.CharField(blank=True, max_length=65, null=True)),
                ('guitar_name', models.CharField(blank=True, max_length=80, null=True)),
                ('guitar_model', models.CharField(blank=True, max_length=80, null=True)),
                ('serial_number', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Guitar',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Manufacturer',
        ),
        migrations.CreateModel(
            name='Appearances',
            fields=[
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='entries.Guitar')),
                ('tour_name', models.CharField(blank=True, max_length=120, null=True)),
                ('album_name', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'Appearances',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='entries.Guitar')),
                ('photo_number', models.IntegerField()),
                ('photo_path', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Photos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Specs',
            fields=[
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='entries.Guitar')),
                ('guitar_spec_id', models.SmallIntegerField()),
                ('production_year', models.SmallIntegerField(blank=True, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('finish', models.CharField(blank=True, max_length=80, null=True)),
                ('body_wood', models.CharField(blank=True, max_length=80, null=True)),
                ('neck_wood', models.CharField(blank=True, max_length=80, null=True)),
                ('fretboard_wood', models.CharField(blank=True, max_length=80, null=True)),
                ('cap_wood', models.CharField(blank=True, max_length=80, null=True)),
                ('neck_pickup', models.CharField(blank=True, max_length=80, null=True)),
                ('middle_pickup', models.CharField(blank=True, max_length=80, null=True)),
                ('bridge_pickup', models.CharField(blank=True, max_length=80, null=True)),
                ('repairs', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Specs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('story_id', models.SmallIntegerField()),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='entries.Guitar')),
                ('story_text', models.TextField()),
                ('where_purchased', models.CharField(blank=True, max_length=80, null=True)),
                ('custom_built', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Story',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='entries.Guitar')),
                ('video_number', models.IntegerField()),
                ('video_path', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Videos',
                'managed': False,
            },
        ),
    ]
