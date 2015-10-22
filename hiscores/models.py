from django.utils import timezone
from django.db import models
from django.db import connection

from utils import skill_names


class Skills(models.Model):
    overall_exp = models.FloatField(default=0)
    overall = models.IntegerField(default=1)

    attack_exp = models.FloatField(default=0)
    attack = models.IntegerField(default=1)

    defence_exp = models.FloatField(default=0)
    defence = models.IntegerField(default=1)

    strength_exp = models.FloatField(default=0)
    strength = models.IntegerField(default=1)

    constitution_exp = models.FloatField(default=0)
    constitution = models.IntegerField(default=1)

    ranged_exp = models.FloatField(default=0)
    ranged = models.IntegerField(default=1)

    prayer_exp = models.FloatField(default=0)
    prayer = models.IntegerField(default=1)

    magic_exp = models.FloatField(default=0)
    magic = models.IntegerField(default=1)

    cooking_exp = models.FloatField(default=0)
    cooking = models.IntegerField(default=1)

    woodcutting_exp = models.FloatField(default=0)
    woodcutting = models.IntegerField(default=1)

    fletching_exp = models.FloatField(default=0)
    fletching = models.IntegerField(default=1)

    fishing_exp = models.FloatField(default=0)
    fishing = models.IntegerField(default=1)

    firemaking_exp = models.FloatField(default=0)
    firemaking = models.IntegerField(default=1)

    crafting_exp = models.FloatField(default=0)
    crafting = models.IntegerField(default=1)

    smithing_exp = models.FloatField(default=0)
    smithing = models.IntegerField(default=1)

    mining_exp = models.FloatField(default=0)
    mining = models.IntegerField(default=1)

    herblore_exp = models.FloatField(default=0)
    herblore = models.IntegerField(default=1)

    agility_exp = models.FloatField(default=0)
    agility = models.IntegerField(default=1)

    thieving_exp = models.FloatField(default=0)
    thieving = models.IntegerField(default=1)

    slayer_exp = models.FloatField(default=0)
    slayer = models.IntegerField(default=1)

    farming_exp = models.FloatField(default=0)
    farming = models.IntegerField(default=1)

    runecrafting_exp = models.FloatField(default=0)
    runecrafting = models.IntegerField(default=1)

    hunter_exp = models.FloatField(default=0)
    hunter = models.IntegerField(default=1)

    construction_exp = models.FloatField(default=0)
    construction = models.IntegerField(default=1)

    summoning_exp = models.FloatField(default=0)
    summoning = models.IntegerField(default=1)

    dungeoneering_exp = models.FloatField(default=0)
    dungeoneering = models.IntegerField(default=1)

    user_name = models.CharField(max_length=30, primary_key=True)

    creation_time = models.DateTimeField(default=timezone.now)

    def get_skills(self):
        """
        Get a player's stats in a list by using Model's '_meta' field.
        Using row_number() to get level_rank of a player in a particular skill

        :return: a list of dictionaries containing skill, rank, level and exp for each skill
        """
        player_stats = []
        cursor = connection.cursor()
        for skill in skill_names:
            level_name = self._meta.get_field(skill).name
            exp_name = self._meta.get_field(skill + '_exp').name

            subquery = "select row_number() OVER(ORDER BY " + exp_name + " DESC, creation_time) as rank,user_name from hiscores_skills"
            query = "select row.rank from (" + subquery + ") as row where row.user_name=%s"
            cursor.execute(query, [self.user_name])

            level_rank = int(cursor.fetchone()[0])
            level = getattr(self, level_name)
            exp = getattr(self, exp_name)

            player_stats.append({
                'name': skill.title(),
                'rank': level_rank,
                'level': level,
                'exp': int(exp),
            })

        return player_stats

    def compare_skills(self, player2):
        """
        Does pretty much same what the above get_skills() does but for both the players at the cost of just one loop.
        Getting a rank using row_number() is a very costly operation. Instead of calling get_skills() twice it's a lot
        efficient to get level_rank of both the players in just one query by providing both usernames in where clause.

        :return: Two lists each containing skill, rank, level and exp in a dictionary for each skill of both players
        """
        player1_stats, player2_stats = [], []
        cursor = connection.cursor()
        for skill in skill_names:
            level_name = self._meta.get_field(skill).name
            exp_name = self._meta.get_field(skill + '_exp').name

            subquery = "select row_number() OVER(ORDER BY " + exp_name + " DESC, creation_time) as rank,user_name from hiscores_skills"
            query = "select row.rank, row.user_name from (" + subquery + ") as row where row.user_name=%s or row.user_name=%s"
            cursor.execute(query, [self.user_name, player2.user_name])
            results = cursor.fetchall()

            # Our query will returns [('rank', 'user_name'), ('rank', 'user_name')]
            # We identify user's rank by checking returned user_name with object's user_name field.
            if results[0][1] == self.user_name:
                player1_level_level_rank, player2_level_level_rank = int(results[0][0]), int(results[1][0])
            else:
                player2_level_level_rank, player1_level_level_rank = int(results[0][0]), int(results[1][0])

            player1_level = getattr(self, level_name)
            player1_exp = getattr(self, exp_name)

            player1_stats.append({
                'name': skill.title(),
                'rank': player1_level_level_rank,
                'level': player1_level,
                'exp': int(player1_exp),
            })

            player2_level = getattr(player2, level_name)
            player2_exp = getattr(player2, exp_name)

            player2_stats.append({
                'name': skill.title(),
                'rank': player2_level_level_rank,
                'level': player2_level,
                'exp': int(player2_exp),
            })

        return player1_stats, player2_stats

    def __str__(self):
        return self.user_name
