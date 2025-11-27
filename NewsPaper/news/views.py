from django.shortcuts import render
# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm
from django.core.paginator import Paginator


class PostsList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['total_news'] = self.get_queryset().count()  # <-- добавляем общее количество
        return context


class SearchNews(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['total_news'] = self.get_queryset().count()  # <-- добавляем общее количество
        return context


class PostDetail(DetailView):
    # Используем другой шаблон — post.html
    template_name = 'post.html'
    queryset = Post.objects.all()


class PostCreate(CreateView):
    template_name = 'add.html'
    form_class = PostForm


# дженерик для редактирования объекта
class PostUpdate(UpdateView):
    template_name = 'add.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы
    # собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
