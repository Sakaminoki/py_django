from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from book.models import BookInfo
def index(request):
    books=BookInfo.objects.all()
    print(books)

    return HttpResponse(books)

######增加数据######
from book.models import BookInfo
# 方式1
book=BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
# 要调用book.save()将数据保存到数据库中

# 方式2，通过objects实现增删改查
BookInfo.objects.create(
    name='开发',
    pub_date='2010-1-2',
    readcount=100
)

######修改数据#####

# 方式1
book=BookInfo.objects.get(id=6)
book.name='开'
book.save()

# 方式2
BookInfo.objects.filter(id=6).update(name='爬虫开发')

######删除数据######

# 方式1

book=BookInfo.objects.get(id=7)

# 物理删除：删除数据   逻辑删除：修改标记为（如is_delete=False）

book.delete()

# 方式2
BookInfo.objects.filter(id=6).delete()

#######查询######

# get查询单一结果，如果不存在会抛出 模型类.DoesNotExits异常
try:
    book = BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

# all查询多个结果
BookInfo.objects.all()
from  book.models import PeopleInfo
PeopleInfo.objects.all()

# count查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count() # 两条语句作用相同

######过滤查询######
# 实现sql中的where功能
# filter过滤出多个结果
# exclude删除掉符合条件剩下的结果
# get得到单一结果

# 模型类名.objects.felter(属性名__运算符=值)       获取n个结果
# 模型类名.objects.exclude(属性名__运算符=值)      获取n个结果
# 模型类名.objects.get(属性名__运算符=值)          获取1个结果，或者异常

#查询编号为1的图书
book=BookInfo.objects.get(id=1)      # 简写形式
book=BookInfo.objects.get(id__exact=1) #完整形式

BookInfo.objects.get(pk=1)          #pk：主键
BookInfo.objects.filter(id=1)
#查询书名包含'湖'的图书

BookInfo.objects.filter(name__contains='湖')

#查询书名以'部'结尾的图书

BookInfo.objects.filter(name__endswith='部')

#查询书名为空的图书

BookInfo.objects.filter(name__isnull=True) # 不会报错
BookInfo.objects.get(name__isnull=True) # 不存在会报错
BookInfo.objects.get(name__isnull=False) # 查询结果有多个，也会报错

#查询编号为1或3或5的图书

BookInfo.objects.filter(id__in=[1,3,5])

#查询编号大于3的图书
# 大于 gt
# 大于等于 gte
# 小于lt
# 小于等于lte
BookInfo.objects.filter(id__gt=3)

#查询编号不等于3的

BookInfo.objects.exclude(id=3)

#查询1980年发表的图书

BookInfo.objects.filter(pub_date__year=1980)

#查询1990年1月1日后发表的图书

BookInfo.objects.filter(pub_date__gt='1990-1-1')

# F对象，用于查询比较两个属性的项
from django.db.models import F
# 使用：2个属性的比较
# 语法形式：以filter为例  模型类名.objects.filter(属性名__运算符=F('第二个属性名'))

# 查询阅读量大于评论量的书籍
BookInfo.objects.filter(readcount__gte=F('commentcount'))

# 查询阅读量大于两倍评论量的书籍
BookInfo.objects.filter(readcount__gte=F('commentcount')*2)

# Q对象，并且查询
# 查询阅读量大于20，且编号小于3
from django.db.models import Q

BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# 上下两个语句等价
BookInfo.objects.filter(readcount__gt=20,id__lt=3)
# 使用Q对象进行并且查询
BookInfo.objects.filter(Q(readcount__gt=20)&Q(id__lt=3))

# 或者查询
# 查询阅读量大于20，或者编号小于3的图书
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

# 查询编号不等于3的书籍
BookInfo.objects.filter(~Q(id=3))
