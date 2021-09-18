from django.db import models
# 这个文件主要是创建数据，django里面不需要在数据库中新建数据
# 在这个文件里面添加你要的数据然后直接迁移数据库就行，具体参考README
# Create your models here.
class Student(models.Model):
    SEX_ITEMS = {
        (1, '男'),
        (2,'女'),
        (0,'未知'),
    }
    STATUS_ITEMS = {
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝'),
    }
    # CharField代表char数据类型IntegerField代表的就是int，简单来说下面这些步骤就是数据库建表
    # 如果你想要添加别的数据也都可以，记住添加之后迁移数据库
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别")
    profession = models.CharField(max_length=128, verbose_name="职业")
    email = models.EmailField(verbose_name="Email")
    qq = models.CharField(max_length=128, verbose_name="QQ")
    phone = models.CharField(max_length=128, verbose_name="电话")
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="审核状态")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '<Student: {}>'.format(self.name)        # 格式化输出，返回的是一个输出结果的对象

    class Meta:
        verbose_name = verbose_name_plural = "学员信息"     # 表名就是学员信息