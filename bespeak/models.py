import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Restaurant(models.Model):
    '''
    餐馆
    '''
    name = models.CharField(max_length=20,unique=True,verbose_name=u'餐馆名称',help_text=u'餐馆名称')
    address = models.CharField(max_length=100,blank=True,null=True,verbose_name=u'餐馆地点',help_text=u'餐馆地址')
    tel = models.CharField(max_length=15,blank=True,null=True,verbose_name=u'订餐电话',help_text=u'手机或者座机')
    desc = models.TextField(blank=True,null=True,verbose_name=u'介绍',help_text=u'餐馆介绍，特色、联系方式')
    isdel = models.BooleanField(default=False,db_index=True,verbose_name=u'是否删除',help_text=u'是否废弃')
    class Meta():
        verbose_name='餐馆'
    def __unicode__(self):
        return self.name



class Dish(models.Model):
    '''
    菜品
    '''
    dishkind = (
        (1,u'凉菜'),
        (2,u'热菜'),
        (3,u'招牌菜'),
        (4,u'盖饭'),
        (5,u'主食'),
        (6,u'饮品'),
        (7,u'点心'),
    )
    name = models.CharField(max_length=20,unique=True,verbose_name=u'菜品名称',help_text=u'菜品名称')
    desc = models.TextField(blank=True,null=True,verbose_name=u'介绍',help_text=u'餐馆介绍，特色、联系方式')
    price = models.DecimalField(decimal_places=10,max_digits=2,verbose_name=u'价格',help_text=u'售价')
    kind = models.IntegerField(choices=dishkind,verbose_name=u'种类',help_text=u'菜品种类')
    isdel = models.BooleanField(default=False,db_index=True,verbose_name=u'是否删除',help_text=u'是否废弃')

    class Meta():
        verbose_name='餐馆'
    def __unicode__(self):
        return self.name


class Order(models.Model):
    '''
    订单
    '''

    type = (
        (1,u'未提交'),
        (2,u'未受理'),
        (3,u'受理成功'),
        (4,u'受理失败'),
    )

    lsh = models.CharField(max_length=50,unique=True,verbose_name=u'订单编号',help_text=u'订单编号')
    date = models.DateField
    user = models.ForeignKey(User,verbose_name=u'订餐人')
    shouli = models.ForeignKey(User,related_name='shouliren',verbose_name=u'订单受理人')
    desc = models.TextField(max_length=50,blank=True,null=True,verbose_name=u'备注')
    price = models.DecimalField(max_digits=2,decimal_places=10,verbose_name=u'订单金额')
    status = models.IntegerField(choices=type,verbose_name=u'订单状态')

    class Meta():
        verbose_name='订单'
    def __unicode__(self):
        return self.lsh


class OrderRecord(models.Model):
    '''
    订单记录
    '''
    order = models.ForeignKey(Order,verbose_name=u'订单')
    dish = models.ForeignKey(Dish,verbose_name=u'订单中的菜品')
    num = models.IntegerField(verbose_name=u'数量')
    price = models.DecimalField(max_digits=2,decimal_places=10,verbose_name=u'单价')
    total = models.DecimalField(max_digits=2,decimal_places=10,verbose_name=u'总价')

    class Meta():
        verbose_name='日报表订单跟踪'
        unique_together=[('order','dish')]

class MoneyRecord(models.Model):
    '''
    押金记录
    '''
    user = models.ForeignKey(User,verbose_name=u'押金人')
    money = models.DecimalField(max_digits=2,decimal_places=10,verbose_name=u'押金金额')
    date = models.DateTimeField(auto_now_add=True,default=datetime.datetime.now,verbose_name=u'发生时间')


class RecommendDaily(models.Model):
    '''
    每日推荐
    '''
    startdate = models.DateField(auto_now=True,verbose_name=u'起始推荐日期')
    enddate = models.DateField(auto_now=True,verbose_name=u'截止推荐日期')
    foods = models.ManyToManyField(Dish,verbose_name=u'点的餐')
    isdel = models.BooleanField(default=False,db_index=True,verbose_name=u'是否删除',help_text=u'是否废弃')





