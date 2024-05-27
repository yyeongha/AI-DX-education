from django.db import models

# Create your models here.

class WebUser(models.Model):
    names = models.CharField(max_length=40)
    telnos = models.CharField(max_length=50)

    def __str__(self): # 장고 관리자 페이지에서 어떤게 보일 것인지
        return self.names 