from django.contrib import admin

from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm

from core.admin.trait import TraitInlineAdmin


class CategoryAdmin(TreeNodeModelAdmin):
    form = TreeNodeForm
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    inlines = [TraitInlineAdmin]
