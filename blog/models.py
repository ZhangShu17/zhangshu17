from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible #兼容python2

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    '''
    分类
    Django 要求模型必须继承models.Model
    Category只需要一个简单的费雷鸣
    CharField 数据类型是字符型
    '''
    name=models.CharField(max_length=100)
    objects=models.Manager()
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    '''
    标签
    '''
    name=models.CharField(max_length=100)
    objects=models.Manager()
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    '''
    文章的数据库表
    '''
    title=models.CharField(max_length=70) 
    body=models.TextField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    excerpt=models.CharField(max_length=70,blank=True) #摘要，允许空值
    category=models.ForeignKey(Category,on_delete=None) #ForeignKey一对多
    tags=models.ManyToManyField(Tag,blank=True)
    author=models.ForeignKey(User,on_delete=None)
    objects=models.Manager()
    def __str__(self):
        return self.title