from django.db import models


class UserInfo(models.Model):
    usrid = models.IntegerField()
    uname = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

    class Meta:
        db_table = "userinfo"
