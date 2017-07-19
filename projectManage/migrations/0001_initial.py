# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-12 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.TextField(null=True)),
                ('name', models.CharField(max_length=64)),
                ('isModified', models.BooleanField(default=True)),
                ('image_file_path', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'bio_chain',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('compound_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('nicknames', models.TextField(null=True)),
                ('formula', models.CharField(max_length=255)),
                ('exact_mass', models.FloatField(null=True)),
                ('mol_mass', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'bio_compound',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compound_Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'bio_compound_gene',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('feature_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128, null=True)),
                ('feature_type', models.CharField(max_length=128, null=True)),
                ('direction', models.CharField(max_length=256, null=True)),
                ('startpos', models.IntegerField(null=True)),
                ('endpos', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'bio_features',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Functions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'bio_functions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('gene_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('nicknames', models.TextField(null=True)),
                ('definition', models.TextField(null=True)),
                ('organism_short', models.CharField(max_length=16)),
                ('organism', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=16)),
                ('ntseq_length', models.IntegerField()),
                ('ntseq', models.TextField(null=True)),
            ],
            options={
                'db_table': 'bio_gene',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('organism_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('organism_short', models.CharField(max_length=16, null=True)),
                ('organism_name', models.TextField(null=True)),
            ],
            options={
                'db_table': 'bio_organism',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('paper_id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('paper_name', models.CharField(max_length=255, null=True)),
                ('paper_file_location', models.CharField(max_length=256, null=True)),
                ('paper_url', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'bio_paper',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Part_Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'bio_part_features',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Part_Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
            ],
            options={
                'db_table': 'bio_part_gene',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Part_Papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'bio_part_papers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Part_Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'bio_part_parameters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Part_Twins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'bio_part_twins',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('part_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ok', models.BooleanField(default=True)),
                ('part_name', models.CharField(max_length=255)),
                ('short_desc', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('part_type', models.CharField(max_length=20, null=True)),
                ('author', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('dominant', models.BooleanField(default=True)),
                ('discontinued', models.IntegerField(null=True)),
                ('part_status', models.CharField(max_length=40, null=True)),
                ('sample_status', models.CharField(max_length=40, null=True)),
                ('p_status_cache', models.CharField(max_length=1000, null=True)),
                ('s_status_cache', models.CharField(max_length=1000, null=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('results', models.CharField(max_length=20, null=True)),
                ('favorite', models.IntegerField(null=True)),
                ('specified_u_list', models.TextField(null=True)),
                ('deep_u_list', models.TextField(null=True)),
                ('deep_count', models.IntegerField(null=True)),
                ('ps_string', models.TextField(null=True)),
                ('scars', models.CharField(max_length=20, null=True)),
                ('barcode', models.CharField(max_length=50, null=True)),
                ('notes', models.TextField(null=True)),
                ('source', models.TextField(null=True)),
                ('nickname', models.CharField(max_length=50, null=True)),
                ('premium', models.IntegerField(null=True)),
                ('categories', models.CharField(max_length=500, null=True)),
                ('sequence', models.TextField(null=True)),
                ('sequence_length', models.IntegerField(null=True)),
                ('part_url', models.CharField(max_length=255, null=True)),
                ('score', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'bio_parts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pathway',
            fields=[
                ('pathway_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('pathway_name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'bio_pathway',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pathway_Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'bio_pathway_compound',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bio_project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('reaction_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True)),
                ('equation', models.TextField(null=True)),
            ],
            options={
                'db_table': 'bio_reactions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reaction_Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isReactant', models.BooleanField(default=False)),
                ('isResultant', models.BooleanField(default=False)),
                ('amount', models.IntegerField(default=1, null=True)),
            ],
            options={
                'db_table': 'bio_reaction_compounds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team_Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'bio_team_parts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('team_id', models.IntegerField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=64)),
                ('year', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'bio_team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Track_Functions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'bio_track_function',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'bio_tracks',
                'managed': False,
            },
        ),
    ]
