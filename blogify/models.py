from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Blogs(models.Model):
    blog_title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # blog_content = models.TextField()  
    blog_content = RichTextField(blank = True, null = True)
    pub_date = models.DateTimeField(auto_now_add=True, null= True)
    likes = models.ManyToManyField(User, related_name = 'blog_posts')

    @property
    def number_of_comments(self):
        return Comment.objects.filter(blogs_connected=self).count()

    def __str__(self):
        return self.blog_title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})

    def get_total_likes(self):
        return self.likes.count()        

class Comment(models.Model):
    blogs_connected = models.ForeignKey(Blogs, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ' | ' + self.blogs_connected.blog_title[:40]