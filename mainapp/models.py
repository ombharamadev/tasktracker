from django.db import models

# Create your models here.

class user_data_app(models.Model):
    name = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    tokenval = models.TextField()
    date_on_reg = models.DateTimeField(auto_now_add=True)


class task_data(models.Model):
    task_create_by  = models.TextField()
    title = models.TextField()
    desc = models.TextField()
    due_date = models.DateField()
    status = models.TextField()
    task_id = models.TextField()
    task_status = models.TextField() # delete or ok to show 

class assing_task(models.Model):
    task_id = models.TextField()
    assign_email = models.TextField()
    status = models.TextField()

