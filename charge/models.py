from django.db import models
import django.utils.timezone as timezone
# Create your models here.
CAR_TYPE = (
    ('0', '小型车'),
    ('1', '中型车'),
    ('2', '大型车'),
)



class Standard(models.Model):
    cartype = models.CharField(max_length=2, choices=CAR_TYPE, verbose_name='车型', default='0')
    day_money = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='白天价格')
    night_money = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='夜间价格')
    all_day_money = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='全天价格')
    time_unit = models.CharField(max_length=20, verbose_name='时间单位')
    start_time = models.TimeField(verbose_name='白天开始计费节点')
    end_time = models.TimeField(verbose_name='白天结束计费节点')
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)


    def __str__(self):
        return self.cartype

    class Meta:
        db_table = 'standard'
        verbose_name = '收费标准'
        verbose_name_plural = verbose_name