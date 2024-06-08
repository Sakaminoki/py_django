from django.db import models

# Create your models here.
"""
1.模型类继承自models.Modol
2.定义属性
    属性名=models.类型(选项)
"""


class BookInfo(models.Model):
    name=models.CharField(max_length=20,unique=True,verbose_name='名称')
    pub_date=models.DateField(null=True,verbose_name='发布日期')
    readcount=models.IntegerField(default=0,verbose_name='阅读量')
    commentcount=models.IntegerField(default=0,verbose_name='评论量')
    is_delete=models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table='bookinfo' # 修改表单的名字
        verbose_name_plural='书籍管理' # admin站点要用

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name_plural = '人物信息'

    def __str__(self):
        return self.name