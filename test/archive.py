def postDetail(request, slug):
    post = Post.objects.get(slug=slug)
    otherPosts = Post.objects.filter(author=post.author)

    prev_post, next_post = get_prev_next_post(post.id)

    allAuthors = Author.objects.all()
    allTags = Tag.objects.all()

    return render(request, 'blog/postDetail.html', {
        'post' : post,
        'otherPosts' : otherPosts,
        'prev_post' : prev_post,
        'next_post': next_post,
        'allAuthors' : allAuthors,
        'allTags' : allTags
    })
# =============================================================================================================================

def get_prev_next_post(currentID):
    prev_post = Post.objects.filter(id__lt=currentID).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=currentID).order_by('id').first()
    return prev_post, next_post


# =============================================================================================================================

def postsByTag(request, tag):
    tag = Tag.objects.get(caption__iexact=tag)
    posts = tag.post_set.all()
    allTags = Tag.objects.all()
    allAuthors = Author.objects.all()

    return render(request, 'blog/postsByTag.html', {
        'tag' : tag,
        'posts' : posts,
        'allTags' : allTags,
        'allAuthors' : allAuthors
    })


# =============================================================================================================================

