from django.db import models
from treenode.models import TreeNodeModel

from core.models import Domain


class Category(TreeNodeModel):
    treenode_display_field = 'name'

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    domain = models.ForeignKey(Domain, blank=True, null=True,
                               related_name='categories',
                               on_delete=models.CASCADE)

    class Meta(TreeNodeModel.Meta):
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # def __str__(self):
    #     representation = ''
    #     if self.parent:
    #         representation += self.parent + ' '
    #     representation += self.name
    #     return representation
