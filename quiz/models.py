from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='quiz-images/', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Question(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.id} - {self.question}'


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.answer}'
