from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dad_name = models.CharField(max_length=60)
    avatar = models.FileField(upload_to=None)

    def __str__(self):
        return 'ФИО: {},{},{}'.format(self.last_name, self.first_name, self.dad_name)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class RubricList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'RubricList'
        verbose_name_plural = 'RubricLists'


class Rubric(models.Model):
    name = models.CharField(max_length=50)
    rubric = models.ForeignKey(RubricList, on_delete=models.CASCADE)
    def __str__(self):
        return '{} {}'.format(self.name, self.rubric)

    class Meta:
        verbose_name = 'Rubric'
        verbose_name_plural = 'Rubrics'


class News(models.Model):
    title = models.CharField(max_length=200)
    announcment = models.CharField(max_length=300)
    text = models.CharField(max_length=1500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rubric = models.ForeignKey(RubricList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}\n' \
               '{}\n' \
               '{}\n' \
               '{}\n' \
               '{}\n'.format(self.id, self.title, self.text, self.author, self.rubric)

