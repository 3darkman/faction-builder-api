from django.contrib import admin
import nested_admin

from core.mixims import InlineEditLinkMixin
from core.models import Trait, TraitChoice, TraitChoicesAbility


class TraitInlineAdmin(admin.TabularInline, InlineEditLinkMixin):
    model = Trait
    fields = ['detail']
    extra = 0
    readonly_fields = ['detail']
    show_change_link = True


class TraitChoicesAbilityInlineAdmin(nested_admin.NestedTabularInline):
    model = TraitChoicesAbility
    fields = ['ability', 'level']
    extra = 0


class TraitChoiceInlineAdmin(nested_admin.NestedStackedInline):
    model = TraitChoice
    extra = 0
    inlines = [TraitChoicesAbilityInlineAdmin]


class TraitAdmin(nested_admin.NestedModelAdmin):
    model = Trait
    inlines = [TraitChoiceInlineAdmin]
