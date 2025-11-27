from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, SearchNews, PostCreate

urlpatterns = [

    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', PostsList.as_view(), name='news_list'),
    path('<int:pk>', PostDetail.as_view() , name='post'),
    path('search/', SearchNews.as_view(), name='news_search'),  # <-- новый путь
    path('add/', PostCreate.as_view(), name='news_add'),
]