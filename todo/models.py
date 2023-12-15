from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField("Name",max_length = 50)
    description = models.TextField("詳細",blank = True)
    deadline = models.DateField("Deadend")
    
    def __str__(self):
        return self.title