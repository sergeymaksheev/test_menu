from django.db import models
from django.urls import reverse

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField('Название', max_length=150)
    parents = models.ForeignKey('self', related_name='head', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return str(self.name)
    

    def get_absolute_url(self):
        return reverse('item', args=[str(self.id)])
    

    def subitem(self):
        return self.head.all()
    

    def get_elder_ids(self):
        return self.parents.get_elder_ids() + [self.parents.id] if self.parents else []


    class Meta:
        ordering = ('name',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'




