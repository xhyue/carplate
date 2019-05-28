from django.db import models

CAR_TYPE = (
    ('0', '小型车'),
    ('1', '中型车'),
    ('2', '大型车'),
)

# Create your models here.
class Car(models.Model):
    type = models.CharField(max_length=2, choices=CAR_TYPE, verbose_name='车型', default='0')
    carplate = models.CharField(max_length=100, verbose_name='车牌号')
    inimg = models.ImageField(upload_to='', verbose_name='驶入图片', default='')
    outimg = models.ImageField(upload_to='', verbose_name='驶出图片', default='', null=True, blank=True)
    in_time = models.DateTimeField(verbose_name='驶入时间', null=True)
    out_time = models.DateTimeField(verbose_name='驶出时间', null=True, blank=True)
    cost = models.DecimalField(verbose_name='费用', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.carplate

    class Meta:
        db_table = 'car'
        verbose_name = '车辆类'
        verbose_name_plural = verbose_name


