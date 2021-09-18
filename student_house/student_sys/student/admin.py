from django.contrib import admin

from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    # 后台数据list_display用来配置页面上展示哪些字段
    list_display = ('id','name','sex','profession','email','qq','phone','status','created_time')
    # 配置页面过滤器，需要通过哪些字段来过滤页面列表
    list_filter = ('sex', 'status', 'created_time')
    # 配置搜索字段
    search_fields = ('name', 'profession')
    # 控制页面布局，限定展示的字段，和展示字段的顺序
    fieldsets = (
        (None, {
            'fields':(
                'name',
                ('sex', 'profession'),
                ('email', 'qq', 'phone'),
                'status',
            )
        }),
    )
# 定义站点的数据表
admin.site.register(Student, StudentAdmin)
