from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # Заголовок поста
    title = models.CharField(max_length=200)
    
    # Зміст поста
    content = models.TextField()
    
    # Автор поста (ForeignKey до вбудованої моделі User)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Дата публікації
    pub_date = models.DateTimeField(auto_now_add=True)
    
    # Категорія поста
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
class Comment(models.Model):
    # Пост, до якого прив'язаний коментар
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    # Автор коментаря
    author = models.CharField(max_length=100)
    
    # Зміст коментаря
    content = models.TextField()
    
    # Дата створення
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
# Create your models here.
