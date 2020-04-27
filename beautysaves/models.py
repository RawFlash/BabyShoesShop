from django.db import models


class Girls(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email,)

