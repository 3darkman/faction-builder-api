from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from core import models


class TraitAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ability
        fields = ('id', 'name')


class TraitChoiceAbilitySerializer(serializers.ModelSerializer):
    ability = TraitAbilitySerializer(many=False, read_only=True)

    class Meta:
        model = models.TraitChoicesAbility
        fields = ('id', 'level', 'ability')


class TraitChoicesSerializer(serializers.ModelSerializer):
    abilities = TraitChoiceAbilitySerializer(many=True, read_only=True)

    class Meta:
        model = models.TraitChoice
        fields = ('id', 'is_all', 'is_armory_choices', 'abilities')


class TraitSerializer(serializers.ModelSerializer):
    choices = TraitChoicesSerializer(many=True, read_only=True)

    class Meta:
        model = models.Trait
        fields = (
            'id',
            'name',
            'point_cost',
            'progress_point_cost',
            'choices'
        )


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    traits = TraitSerializer(many=True)

    class Meta:
        model = models.Category
        fields = ('id', 'name', 'description', 'children',
                  'traits')
