from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

# from django.core.cache import cache
# Create your views here.
from .forms import PostCommentsForm
from .models import Post, Author, Tag, Comments


biodata = {
    'skills': ['Python & Django',
            'HTML & CSS',
            'JavaScript & jQuery',
            'Git & Version Control',
            'Problem Solving',
            ],
    'hobbies': [
        'Reading tech blogs',
        'Exploring new technologies',
        'Playing video games',
        'Photography',
        'Traveling and exploring new cultures',
    ],
    'projects': [
        'Blog Website using Django',
        'Portfolio Website using HTML, CSS, and JavaScript',
        'Task Management App using Django REST Framework',
        'book Store Using Django And SQLite',
    ]
}


class GetAuthorAndTagView:
    def get_authors_and_tags(self):
        # cacheKey = ('get_authors_and_tags')
        # cachedData = cache.get(cacheKey)

        # if cachedData:
        #     allAuthors , allTags = cachedData
        #     return allAuthors , allTags
        # else:
            allAuthors = list(Author.objects.all())
            allTags = list(Tag.objects.all())

            # cache.set(cacheKey, (allAuthors, allTags), timeout= 86400)

            return allAuthors, allTags


class HomeView(TemplateView, GetAuthorAndTagView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        allAuthors, allTags = self.get_authors_and_tags()

        context.update({
            'allAuthors' : allAuthors,
            'allTags' : allTags
        })
        return context


def bio(request):
    return render(request, 'blog/bio.html', biodata)


class AllPostsView(ListView, GetAuthorAndTagView):
    template_name = 'blog/allposts.html'
    model = Post

    context_object_name = 'allPosts'

    def get_queryset(self):
        queryset = super().get_queryset()
        retQuerySet = queryset.all().order_by('-date')[:3]
        return retQuerySet


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        allAuthors, allTags = self.get_authors_and_tags()
        context.update({
            'allAuthors' : allAuthors,
            'allTags' : allTags
        })
        return context


class PostDetailView(View, GetAuthorAndTagView):

    def get_context_data(self, post, form=None):
        other_posts = Post.objects.filter(author=post.author)
        prev_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
        next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
        post_comments = Comments.objects.filter(post=post, reply__isnull=True).order_by('-date')
        totallComments = Comments.objects.filter(post=post).count()

        allAuthors, allTags = self.get_authors_and_tags()

        context = {
            "post": post,
            "form": form or PostCommentsForm(),
            "postComments": post_comments,
            "totallComments" : totallComments,
            "otherPosts": other_posts,
            "prev_post": prev_post,
            "next_post": next_post,
            "allAuthors": allAuthors,
            "allTags": allTags,
        }


        return context
    

    def get(self, request, slug):
    
        post = get_object_or_404(Post, slug=slug)
        context = self.get_context_data(post=post)
        
        return render(request, 'blog/postDetail.html', context)


    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = PostCommentsForm(request.POST)
        
        if form.is_valid():

            # if form.cleaned_data.get("temp"):
            #     return HttpResponse("Done")
            formRecord = Comments(
                userName=form.cleaned_data['userName'],  # Use cleaned_data for validated data
                comment=form.cleaned_data['comment'],    # Use cleaned_data for validated data
                post=post
            )
            formRecord.save()

            return redirect('postDetailUrl', slug=slug)
        else:
            context = self.get_context_data(post=post, form=form)
            return render(request, 'blog/postDetail.html', context)


class PostsByTagView(TemplateView, GetAuthorAndTagView):
    template_name = 'blog/postsByTag.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = kwargs.get('tag')

        tag = Tag.objects.get(caption__iexact=tag)
        posts = tag.post_set.all()

        allAuthors, allTags = self.get_authors_and_tags()

        context["tag"] = tag
        context["posts"] = posts
        context["allAuthors"] = allAuthors
        context["allTags"] = allTags
        return context


class GetAuthorInfoView(TemplateView, GetAuthorAndTagView):

    def get_author_info(self, authorName):
        fullName = authorName.split()
        if len(fullName) > 2:
            firstName = fullName[0]
            lastName = " ".join(fullName[1:])
        else:
            firstName = fullName[0]
            lastName = fullName[1]
        
        author = Author.objects.get(firstName__iexact=firstName, lastName__iexact=lastName)

        return author


class AuthorAllPostView(GetAuthorInfoView):
    template_name = 'blog/authorAllPosts.html'
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authorName = kwargs.get('author')
        author= self.get_author_info(authorName)

        allPosts = Post.objects.filter(author=author)
        allAuthors, allTags = self.get_authors_and_tags()


        context.update({
            'author' : author,
            'allPosts' : allPosts,
            'allAuthors' : allAuthors,
            'allTags' : allTags
        })
        return context
    

class AuthorBioView(GetAuthorInfoView):
    template_name = 'blog/authorBio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authorName = kwargs.get('authorName')

        author = self.get_author_info(authorName)
        allAuthors, allTags = self.get_authors_and_tags()

        context.update({
            'author' : author,
            'allAuthors' : allAuthors,
            'allTags' : allTags
        })
        return context
    