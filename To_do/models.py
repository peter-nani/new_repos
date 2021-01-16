from django.db import models


class To_Do(models.Model):
    do_it = models.CharField(max_length=300)
    def __str__(self):
        return self.do_it
