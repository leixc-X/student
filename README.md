

# 学员管理系统

student 这个系统分为前后端，前端就是展示数据并且可以提交数据，后台用来管理数据（增查删改）

## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
  - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
  - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)

### 上手指南

README这个文件是关于本项目的介绍，请认真阅读



###### 开发前的配置要求

1. python3.0以上
2. 本项目是建立在虚拟环境上的（利用自带的venv文件）需要安装虚拟环境，非常简单装个包就行https://www.cnblogs.com/lovele-/p/8719126.html （参考这个博客）

###### **安装步骤**

1. 虚拟环境安装好后cmd进入项目文件 输入student-env\Scripts\activate 激活虚拟环境
2. pip install django==1.11 安装django，我用的是1.11版本
3. 进入manage.py这个文件夹里面，输入命令 python manage.py runserver 运行服务器
4. 浏览器打开输入127.0.0.1和127.0.0.1/admin 即可进入系统 （前者是前台展示，后者是管理页面）



### 文件目录说明
eg:

```
filetree 
├── idea
├── README.md
├── student-env
├── venv
├── student_house
│  ├── student_sys
│  │  ├── student
│  │  └──--- admin.py
│  │  └──--- apps.py
│  │  └──--- forms	.py
│  │  └──--- models.py
│  │  └──--- tests.py
│  │  └──--- views.py
│  │  └──--- templates
│  │  └──------- index.html
│  │  └── student_sys
│  │  └──--- setting.py
│  │  ├── db.sqlite3
│  │  └── manage.py


```

student-env这个文件是用venv这个文件创建的虚拟环境

student_house是项目文件

student文件里面是django自动生成文件admin.py我们来写后台管理页面 forms.py是我创建的主要实现了 一个前台插入数据的功能 models.py这个文件就是建表，我们一般在这里面添加我们所需要的数据然后迁移数据库views.py提交数据给后台系统，利用http协议. templates这个文件里面放的是前端页面，因为只需要一个index主页展示数据，所以就只有index。如果你需要别的页面自行创建，但是记住一定要在这个文件里面。setting.py这个文件主要是对django项目的一些设置，比如时区，语言等等.我都设置好了。db.sqlite3这是数据库文件， 我没有用mysql数据库，而是用了这个数据库文件简单方便，如果你想用mysql也可以，修改setting文件里面数据库信息，然后输入两行命令迁移数据库就可以了。 manage.py是django的管理文件，很重要，很多操作都需要用到它比如启动服务器，创建一个app等等。





我在里面一直提到的迁移数据库，这个非常重要，具体步骤

- `cd student_house/student_sys/`
- `python manage.py makemigrations` 创建迁移文件
- `python manage.py migrate` 创建表
- `python manage.py createsuperuser` 根据提示，输出用户名，邮箱，密码
- 启动项目: `python manage.py runserver`，访问: [http://127.0.0.1:8000，看到一个提示页，这是因为我们还没开发首页。我们可以进入到admin的页面](http://127.0.0.1:8000，看到一个提示页，这是因为我们还没开发首页。我们可以进入到admin的页面/): http://127.0.0.1:8000/admin/。用你创建好的账户登录，就能看到一个完整的带有CURD的后台了。

关于整个项目的所有步骤全部记录在个连接里面

https://github.com/the5fire/django-practice-book/tree/master/chapter3



### 开发的架构 

django

### 部署

暂无

### 使用到的框架

- [xxxxxxx](https://jquery.com)
- [xxxxxxx](https://laravel.com)

### 贡献者

请阅读**CONTRIBUTING.md** 查阅为该项目做出贡献的开发者。

#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

lxc

### 版权说明

没啥版权，你们拿着玩吧

### 鸣谢


- lxc

  


