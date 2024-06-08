from django.db import models

# Create your models here.
"""
1.模型类继承自models.Modol
2.定义属性
    属性名=models.类型(选项)
"""
class Bookinfo(models.Model):
    name=models.CharField(max_length=20)
    