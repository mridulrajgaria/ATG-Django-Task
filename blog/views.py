from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    blogs = BlogPost.objects.filter(is_draft=False).order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

@login_required
def create_blog_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('my_blogs')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog.html', {'form': form})

@login_required
def my_blogs_view(request):
    blogs = BlogPost.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/my_blogs.html', {'blogs': blogs})

def category_blogs_view(request, category):
    blogs = BlogPost.objects.filter(category=category, is_draft=False).order_by('-created_at')
    return render(request, 'blog/category_blogs.html', {'blogs': blogs, 'category': category})
