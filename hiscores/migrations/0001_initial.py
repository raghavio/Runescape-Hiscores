# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('overall_exp', models.FloatField(default=0)),
                ('overall', models.IntegerField(default=1)),
                ('attack_exp', models.FloatField(default=0)),
                ('attack', models.IntegerField(default=1)),
                ('defence_exp', models.FloatField(default=0)),
                ('defence', models.IntegerField(default=1)),
                ('strength_exp', models.FloatField(default=0)),
                ('strength', models.IntegerField(default=1)),
                ('constitution_exp', models.FloatField(default=0)),
                ('constitution', models.IntegerField(default=1)),
                ('ranged_exp', models.FloatField(default=0)),
                ('ranged', models.IntegerField(default=1)),
                ('prayer_exp', models.FloatField(default=0)),
                ('prayer', models.IntegerField(default=1)),
                ('magic_exp', models.FloatField(default=0)),
                ('magic', models.IntegerField(default=1)),
                ('cooking_exp', models.FloatField(default=0)),
                ('cooking', models.IntegerField(default=1)),
                ('woodcutting_exp', models.FloatField(default=0)),
                ('woodcutting', models.IntegerField(default=1)),
                ('fletching_exp', models.FloatField(default=0)),
                ('fletching', models.IntegerField(default=1)),
                ('fishing_exp', models.FloatField(default=0)),
                ('fishing', models.IntegerField(default=1)),
                ('firemaking_exp', models.FloatField(default=0)),
                ('firemaking', models.IntegerField(default=1)),
                ('crafting_exp', models.FloatField(default=0)),
                ('crafting', models.IntegerField(default=1)),
                ('smithing_exp', models.FloatField(default=0)),
                ('smithing', models.IntegerField(default=1)),
                ('mining_exp', models.FloatField(default=0)),
                ('mining', models.IntegerField(default=1)),
                ('herblore_exp', models.FloatField(default=0)),
                ('herblore', models.IntegerField(default=1)),
                ('agility_exp', models.FloatField(default=0)),
                ('agility', models.IntegerField(default=1)),
                ('thieving_exp', models.FloatField(default=0)),
                ('thieving', models.IntegerField(default=1)),
                ('slayer_exp', models.FloatField(default=0)),
                ('slayer', models.IntegerField(default=1)),
                ('farming_exp', models.FloatField(default=0)),
                ('farming', models.IntegerField(default=1)),
                ('runecrafting_exp', models.FloatField(default=0)),
                ('runecrafting', models.IntegerField(default=1)),
                ('hunter_exp', models.FloatField(default=0)),
                ('hunter', models.IntegerField(default=1)),
                ('construction_exp', models.FloatField(default=0)),
                ('construction', models.IntegerField(default=1)),
                ('summoning_exp', models.FloatField(default=0)),
                ('summoning', models.IntegerField(default=1)),
                ('dungeoneering_exp', models.FloatField(default=0)),
                ('dungeoneering', models.IntegerField(default=1)),
                ('user_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
    ]
