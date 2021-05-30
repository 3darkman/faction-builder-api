from django.db import models

from core.models import Ability, Category


class Trait(models.Model):
    name = models.CharField(max_length=255)
    point_cost = models.IntegerField()
    progress_point_cost = models.IntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="traits")

    def detail(self):
        name = self.name
        if self.point_cost:
            if self.point_cost > 0:
                name = f'{self.name} {self.point_cost}pts'

        ability_list = []
        abilities = ' '
        choices = self.choices.all()
        if choices:
            for choice in choices:
                choice_abilities = choice.abilities.all()
                if choice_abilities:
                    for ability in choice_abilities:
                        if ability.level:
                            ability_list.append(f'{ability.ability.name} {ability.level}')
                        else:
                            ability_list.append(f'{ability.ability.name}')
        abilities = ', '.join(ability_list)
        name = f'{name}: {abilities}'
        return name

    def __str__(self):
        return self.detail()


class TraitChoice(models.Model):
    is_all = models.BooleanField()
    is_armory_choices = models.BooleanField()

    trait = models.ForeignKey(Trait, on_delete=models.CASCADE,
                              related_name='choices')

    def __str__(self):
        return self.trait.name


class TraitChoicesAbility(models.Model):
    level = models.IntegerField(blank=True, null=True)

    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    choice = models.ForeignKey(TraitChoice, on_delete=models.CASCADE,
                               related_name='abilities')

    def __str__(self):
        if self.level:
            return f'{self.choice} - {self.ability.name} {self.level}'
        else:
            return f'{self.choice} - {self.ability.name}'
