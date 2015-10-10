# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import hiscores.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('overall_exp', hiscores.models.ExpField(default=0)),
                ('overall', hiscores.models.LevelField(default=1)),
                ('attack_exp', hiscores.models.ExpField(default=0)),
                ('attack', hiscores.models.LevelField(default=1)),
                ('defence_exp', hiscores.models.ExpField(default=0)),
                ('defence', hiscores.models.LevelField(default=1)),
                ('strength_exp', hiscores.models.ExpField(default=0)),
                ('strength', hiscores.models.LevelField(default=1)),
                ('constitution_exp', hiscores.models.ExpField(default=0)),
                ('constitution', hiscores.models.LevelField(default=1)),
                ('ranged_exp', hiscores.models.ExpField(default=0)),
                ('ranged', hiscores.models.LevelField(default=1)),
                ('prayer_exp', hiscores.models.ExpField(default=0)),
                ('prayer', hiscores.models.LevelField(default=1)),
                ('magic_exp', hiscores.models.ExpField(default=0)),
                ('magic', hiscores.models.LevelField(default=1)),
                ('cooking_exp', hiscores.models.ExpField(default=0)),
                ('cooking', hiscores.models.LevelField(default=1)),
                ('woodcutting_exp', hiscores.models.ExpField(default=0)),
                ('woodcutting', hiscores.models.LevelField(default=1)),
                ('fletching_exp', hiscores.models.ExpField(default=0)),
                ('fletching', hiscores.models.LevelField(default=1)),
                ('fishing_exp', hiscores.models.ExpField(default=0)),
                ('fishing', hiscores.models.LevelField(default=1)),
                ('firemaking_exp', hiscores.models.ExpField(default=0)),
                ('firemaking', hiscores.models.LevelField(default=1)),
                ('crafting_exp', hiscores.models.ExpField(default=0)),
                ('crafting', hiscores.models.LevelField(default=1)),
                ('smithing_exp', hiscores.models.ExpField(default=0)),
                ('smithing', hiscores.models.LevelField(default=1)),
                ('mining_exp', hiscores.models.ExpField(default=0)),
                ('mining', hiscores.models.LevelField(default=1)),
                ('herblore_exp', hiscores.models.ExpField(default=0)),
                ('herblore', hiscores.models.LevelField(default=1)),
                ('agility_exp', hiscores.models.ExpField(default=0)),
                ('agility', hiscores.models.LevelField(default=1)),
                ('thieving_exp', hiscores.models.ExpField(default=0)),
                ('thieving', hiscores.models.LevelField(default=1)),
                ('slayer_exp', hiscores.models.ExpField(default=0)),
                ('slayer', hiscores.models.LevelField(default=1)),
                ('farming_exp', hiscores.models.ExpField(default=0)),
                ('farming', hiscores.models.LevelField(default=1)),
                ('runecrafting_exp', hiscores.models.ExpField(default=0)),
                ('runecrafting', hiscores.models.LevelField(default=1)),
                ('hunter_exp', hiscores.models.ExpField(default=0)),
                ('hunter', hiscores.models.LevelField(default=1)),
                ('construction_exp', hiscores.models.ExpField(default=0)),
                ('construction', hiscores.models.LevelField(default=1)),
                ('summoning_exp', hiscores.models.ExpField(default=0)),
                ('summoning', hiscores.models.LevelField(default=1)),
                ('dungeoneering_exp', hiscores.models.ExpField(default=0)),
                ('dungeoneering', hiscores.models.LevelField(default=1)),
                ('user_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
    ]
