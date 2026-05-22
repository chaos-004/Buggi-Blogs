from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, Category, Tag, Comment
from .forms import CommentForm
from django.db.models import Count


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        return Post.objects.filter(status='published').select_related('category', 'author').prefetch_related('tags')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = Post.objects.filter(status='published', featured_image__isnull=False)[:3]
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Post.objects.filter(status='published')[:5]
        context['tags'] = Tag.objects.all()
        return context


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 9
    
    def get_queryset(self):
        return Post.objects.filter(status='published').select_related('category', 'author').prefetch_related('tags')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'
    
    def get_queryset(self):
        return Post.objects.filter(status='published').select_related('category', 'author').prefetch_related('tags')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.get_comments()
        context['comment_form'] = CommentForm()
        context['related_posts'] = Post.objects.filter(
            status='published',
            category=post.category
        ).exclude(id=post.id)[:3]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 9
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(status='published', category=self.category).select_related('category', 'author').prefetch_related('tags')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class TagPostListView(ListView):
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'
    paginate_by = 9
    
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.objects.filter(status='published', tags=self.tag).select_related('category', 'author').prefetch_related('tags')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class SearchView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    paginate_by = 9
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Post.objects.filter(
                status='published'
            ).filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(summary__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct().select_related('category', 'author').prefetch_related('tags')
        return Post.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class AboutView(View):
    def get(self, request):
        categories = Category.objects.all()
        tags = Tag.objects.all()
        total_posts = Post.objects.filter(status='published').count()
        total_categories = categories.count()
        total_tags = tags.count()
        
        context = {
            'categories': categories[:10],
            'tags': tags[:15],
            'total_posts': total_posts,
            'total_categories': total_categories,
            'total_tags': total_tags,
        }
        return render(request, 'blog/about.html', context)


class AddCommentView(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug, status='published')
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been submitted and is awaiting moderation.')
            return redirect('blog:post_detail', slug=slug)
        
        messages.error(request, 'There was an error with your comment. Please try again.')
        return redirect('blog:post_detail', slug=slug)

