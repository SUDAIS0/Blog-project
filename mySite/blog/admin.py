from django.contrib import admin

# Register your models here.
from .models import Post, Author, Tag, Comments

class PostAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {
        'slug' : ('blogTitle',)
    }
    list_filter = ('author','date', 'captions',)
    list_display = ('id','blogTitle', 'author', 'date',)


admin.site.register(Post, PostAdmin)


class AuthorAdmin(admin.ModelAdmin):

    # list_filter = ('date',)
    list_display = ('fullName', 'email',)

admin.site.register(Comments)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)