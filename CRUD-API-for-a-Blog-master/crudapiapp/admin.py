from django.contrib import admin
from .models import BlogData

class AdminBlog(admin.ModelAdmin):
    list_display=['title','content','author','creation_date','last_update_date']

admin.site.register(BlogData,AdminBlog)