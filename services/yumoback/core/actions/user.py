from ..models import user

def login(usrid:int):
    try:
        user.UserInfo.objects.get(usrid=usrid)
    except user.UserInfo.DoesNotExist as e:
        user.UserInfo.objects.create(usrid=usrid, uname="yumo")
    return True


def registe(usrid, uname, passwd):
    pass