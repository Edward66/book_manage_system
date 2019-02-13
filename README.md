# 开发环境

- Python（3.6.1）
- Django（2.1.5）

# 配置开发环境
## 使用虚拟环境(virturalenv)
```
pip install virtualenv
mkvirtualenv django-learn -p 'python3.6'
workon django-learn
```

# 生成表结构
```
./manage.py makemigrations
./manage.py migrate
```

# 启动项目
./manage.py runserver

# ORM关系表
一对一（author, authordetail）

一对多（book, publisher）

多对多（book,author）

# 实现的功能
1. 图书、作者、管理员的增删改查
2. 使用django自带的forms进行验证（ModelForm和Form）
3. 点击作者会列出作者出版的书籍，点击出版社会列出该出版社出版的书籍
4. 修改图书时，用的是ajax请求
5. 分页功能
6. 注册、登陆功能，不登陆无法进入图书管理系统（用中间件实现）

# 用户登录信息
账号：edward
密码：112233

# 程序运行效果
![index.png](https://github.com/Edward66/book_manage_system/blob/master/index.png)


