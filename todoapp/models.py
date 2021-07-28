from django.db import models

# Create your models here.
class AddTask(models.Model):
    taskname=models.CharField(max_length=20)
    description=models.TextField(max_length=100,default="")
    status=models.BooleanField(default=False)
    def __repr__(self) -> str:
        return self.taskname
