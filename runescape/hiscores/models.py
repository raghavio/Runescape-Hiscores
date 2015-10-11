from django.db import models
from django.db import connection

class ExpField(models.FloatField):

    def __init__(self, *args, **kwargs):
        # Have a default "default" set to 0.
        if kwargs.get('default') is None:
            kwargs['default'] = 0

        super(ExpField, self).__init__(*args, **kwargs)


class LevelField(models.IntegerField):

    def __init__(self, *args, **kwargs):
        # Have a default "default" set to 1.
        if kwargs.get('default') is None:
            kwargs['default'] = 1

        self.exp_field = kwargs.pop('exp_field', None)

        super(LevelField, self).__init__(*args, **kwargs)

class Skills(models.Model):

    overall_exp = ExpField()
    overall = LevelField(exp_field=overall_exp)

    attack_exp = ExpField()
    attack = LevelField(exp_field=attack_exp)

    defence_exp = ExpField()
    defence = LevelField(exp_field=defence_exp)

    strength_exp = ExpField()
    strength = LevelField(exp_field=strength_exp)

    constitution_exp = ExpField()
    constitution = LevelField(exp_field=constitution_exp)

    ranged_exp = ExpField()
    ranged = LevelField(exp_field=ranged_exp)

    prayer_exp = ExpField()
    prayer = LevelField(exp_field=prayer_exp)

    magic_exp = ExpField()
    magic = LevelField(exp_field=magic_exp)

    cooking_exp = ExpField()
    cooking = LevelField(exp_field=cooking_exp)

    woodcutting_exp = ExpField()
    woodcutting = LevelField(exp_field=woodcutting_exp)

    fletching_exp = ExpField()
    fletching = LevelField(exp_field=fletching_exp)

    fishing_exp = ExpField()
    fishing = LevelField(exp_field=fishing_exp)

    firemaking_exp = ExpField()
    firemaking = LevelField(exp_field=firemaking_exp)

    crafting_exp = ExpField()
    crafting = LevelField(exp_field=crafting_exp)

    smithing_exp = ExpField()
    smithing = LevelField(exp_field=smithing_exp)

    mining_exp = ExpField()
    mining = LevelField(exp_field=mining_exp)

    herblore_exp = ExpField()
    herblore = LevelField(exp_field=herblore_exp)

    agility_exp = ExpField()
    agility = LevelField(exp_field=agility_exp)

    thieving_exp = ExpField()
    thieving = LevelField(exp_field=thieving_exp)

    slayer_exp = ExpField()
    slayer = LevelField(exp_field=slayer_exp)

    farming_exp = ExpField()
    farming = LevelField(exp_field=farming_exp)

    runecrafting_exp = ExpField()
    runecrafting = LevelField(exp_field=runecrafting_exp)

    hunter_exp = ExpField()
    hunter = LevelField(exp_field=hunter_exp)

    construction_exp = ExpField()
    construction = LevelField(exp_field=construction_exp)

    summoning_exp = ExpField()
    summoning = LevelField(exp_field=summoning_exp)

    dungeoneering_exp = ExpField()
    dungeoneering = LevelField(exp_field=dungeoneering_exp)

    user_name = models.CharField(max_length=30, primary_key=True)

    def get_skills(self):
        # Returns a list of dictionnaries containing name, level and XP
        # for each of the model's skills.
        skill_values = []

        # Iterate over the model's fields.
        for field in self._meta.get_fields():
            if isinstance(field, LevelField):
                level = getattr(self, field.name)
                exp = getattr(self, field.exp_field.name)
                players = Skills.objects.order_by("-%s" % field.exp_field.name).all()
                rank = [i+1 for i, player in enumerate(players) if player.user_name == self.user_name][0]
                skill_values.append({
                    'name': field.name.title(),
                    'rank' : rank,
                    'level': level,
                    'exp': int(exp),
                })

        return skill_values

    def __str__(self):
        return self.user_name
