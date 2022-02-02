from django.db import models

# Create your models here.
class details(models.Model):
    MEMORY = (
        ('4Gb','4Gb'),
        ('8Gb','8Gb'),
        ('16Gb','16Gb'),
    )
    userID = models.CharField(max_length=30,default="admin")
    deviceID = models.CharField(max_length=20)
    uptime = models.IntegerField(default=0)
    cpu_usage = models.PositiveIntegerField(default=0)
    memory_usage = models.CharField(max_length=4,choices=MEMORY)
    disk_partitions_usage = models.CharField(max_length=120)

    def __str__(self):
        return self.userID

