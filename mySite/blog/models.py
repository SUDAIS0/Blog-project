from django.db import models

from django.utils.text import slugify
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
# Create your models here.

class Tag(models.Model):

    caption = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.caption
    

class Author(models.Model):

    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, unique=True)
    about = models.TextField(null=True)
    
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    def __str__(self):
        return f"{self.firstName}"
    
class Comments(models.Model):

    userName = models.CharField(max_length=70)
    comment = models.TextField()
    date = models.DateField(auto_now=True)
    post = models.ForeignKey("Post", verbose_name=("post"), on_delete=models.CASCADE, related_name='comments')
    reply = models.ForeignKey("self", verbose_name=("reply"), on_delete=models.CASCADE, related_name='replies', null=True, blank=True)

    
    def __str__(self):
        if self.reply:
            return f"Reply to {self.reply.userName}: {self.comment}"
        return f"Name: {self.userName}\nComment: {self.comment}\nReplies: {self.replies.count()}"
    


class Post(models.Model):

    blogTitle = models.CharField(max_length=60)
    author = models.ForeignKey(Author, verbose_name=("Author"), on_delete=models.SET_NULL, null=True, related_name='posts')
    excerpt = models.CharField(max_length=150)
    imageName = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(default='', null=False, db_index=True)
    captions = models.ManyToManyField(Tag, verbose_name=("captions"), blank=True)
    content = models.TextField()

    def save(self, *args, **kwargs):

        self.slug = slugify(self.blogTitle)
        super().save(*args, **kwargs)

    def __str__(self):
        captions = ", ".join(tag.caption for tag in self.captions.all())
        comments = ", ".join(str(comment) for comment in self.comments.all())

        return f"{self.id} Blog Title = {self.blogTitle}\nBlog Author = {self.author}\nExcerpt = {self.excerpt}\nDate = {self.date}\nSlug = {self.slug}\Captions = {captions},\nContent = {self.content}\nComments = {comments}"
    
# class AuthorRegistration(models.Model):

#     firstName = models.CharField(max_length=30)
#     lastName = models.CharField(max_length=30)
#     userName = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=254, unique=True)
#     about = models.TextField(null=True)
#     profilePicture = models.ImageField(blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    
#     def fullName(self):
#         return f"{self.firstName} {self.lastName}"

#     def __str__(self):
#         return f"{self.firstName}"

# class UserRegistration(model.Model):

#     firstName = models.CharField(max_length=30)
#     lastName = models.CharField(max_length=30)
#     password = models.CharField(max_length=50)
#     userName = models.CharField(max_length=50, unique=True, validators=[RegexValidator(
#         regex=r'^^[_a-zA-Z0-9]+(_{1,2}[a-zA-Z0-9]*)*$',
#         message='Enter Valid User Name (Its should contain letters and numbers with only one or two consective underscores.)',
#         code='Invalid User Name'
#     )])
#     email = models.EmailField(max_length=254, unique=True)
#     age = models.IntegerField(validators=[MinLengthValidator(6)])



