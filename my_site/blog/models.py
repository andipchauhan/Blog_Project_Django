from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()
    
class Tag(models.Model):
    caption = models.CharField(max_length=50)
    
    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=300)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tag = models.ManyToManyField(Tag, related_name="posts")
    
    
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=254)
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    