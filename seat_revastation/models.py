from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Seat(models.Model):
    code = models.CharField(max_length = 255)
    is_disable = models.BooleanField(default = False)
    room = models.ForeignKey(Room,on_delete = models.CASCADE,related_name="seats")
    def __str__(self):
        if self.is_disable:
            return '{} (disable)'.format(self.code)
        return self.code