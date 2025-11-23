import django_filters
from .models import Post
from django import forms

class PostFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(
        field_name='date_time',
        lookup_expr='date__gte',
        label='Позже',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    name = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='По заголовку'
    )

    author = django_filters.CharFilter(
        field_name='author__user__username',
        lookup_expr='icontains',
        label='Автор'
    )

    class Meta:
        model = Post
        fields = ['date', 'name', 'author']