from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=64,unique=True)
    owner = models.ForeignKey('User', default='null',verbose_name='管理员')
    remarks = models.CharField(max_length=50,blank=True,verbose_name='备注')

    class Meta:
        verbose_name = '组'

    def __str__(self):
        return self.group_name