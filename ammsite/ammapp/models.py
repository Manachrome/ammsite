from django.db import models

# Описание моделей
#TextField -- текстовое поле, IntegerField -- численное поле
class Group (models.Model):
    number = models.IntegerField()
    course = models.IntegerField()
    level = models.TextField()
    direction = models.TextField(blank=True)
    #__str__ возврат текстового значения модели
    def __str__(self):
        return  str(self.number)+" группа "+str(self.course)+"й курс "+self.level

class Student (models.Model):
    #ForeignKey ссылка на другую таблицу
    group = models.ForeignKey(Group, related_name="student")
    name = models.TextField()
    b_date = models.DateField()
    def __str__(self):
        return str(self.group) + " " +self.name
