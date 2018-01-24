from django.db import models

from dailyfresh.db.base_model import Base_Model


# Create your models here.
class PassportManager(models.Manager):
    def add_one_passport(self, username, password, email):
        model_class = self.model
        obj = model_class(username=username, password=password, email=email)
        obj.save()
        return obj


class Passport(Base_Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱地址')

    objects = PassportManager()

    class Meta:
        db_table = 's_user_account'
