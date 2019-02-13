from django.db import models


class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField(null=True)
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)


class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    authordetail = models.OneToOneField(to="AuthorDetail", to_field='nid', on_delete=models.CASCADE)  # 加引号会从全局去找

    @classmethod
    def get_all(cls):  # 后期修改需求时，只需要修改get_all函数即可
        return cls.objects.all()

    def __str__(self):
        return self.name


class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    @classmethod
    def get_all(cls):  # 后期修改需求时，只需要修改get_all函数即可
        return cls.objects.all()

    def __str__(self):
        return self.name


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, unique=True)
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.ForeignKey(to="Publish", to_field='nid', on_delete=models.CASCADE)
    authors = models.ManyToManyField(to='Author')

    @classmethod
    def get_all(cls):  # 后期修改需求时，只需要修改get_all函数即可
        return cls.objects.all()
