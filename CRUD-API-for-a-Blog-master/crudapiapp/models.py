from django.db import models

class BlogData(models.Model):
    blog_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.CharField(max_length=100)
    creation_date=models.DateTimeField(auto_now_add=True)
    last_update_date=models.DateTimeField(auto_now=True)