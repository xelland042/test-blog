from django.db import models
from django.contrib.auth import get_user_model
from post.managers import TagCustomManager

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='tags', blank=True)

    def __str__(self):
        return f'{self.title}'


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    objects = TagCustomManager()

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    author = models.CharField(max_length=100)
    comment_field = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="replies", null=True, blank=True)
    is_reply = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.post} - {self.author}'
