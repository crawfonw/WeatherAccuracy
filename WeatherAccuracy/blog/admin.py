from django.contrib import admin

from WeatherAccuracy.shared_admin import FengShuiAdmin
from models import BlogPost

class BlogPostAdmin(FengShuiAdmin):
    list_display = ('author', 'title', 'post_date', 'is_draft',)
    list_filter = ('is_draft',)
    
    search_fields = ('author', 'title',)
    
admin.site.register(BlogPost, BlogPostAdmin)