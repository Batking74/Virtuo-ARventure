from django.db import models

# Create your models here for database.

# Creating a class called toDoList that extends Model
class ToDoList(models.Model):
    # Defining Database Schema Columns
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text



# When done modifying models file tell django that you've modified it by using this command: "python manage.py makemigrations appFileName". This command is similar to adding all files to the staging area in git. To actually apply the change use this command after: python manage.py migrate