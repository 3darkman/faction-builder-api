from django.contrib import admin
from core import models

from .category import CategoryAdmin
from .trait import TraitAdmin
from .user import UserAdmin


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Ability)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Trait, TraitAdmin)
admin.site.register(models.Domain)
admin.site.register(models.FactionType)
admin.site.register(models.CategorySlot)
admin.site.register(models.StartingProfile)
