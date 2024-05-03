from django.urls import path
# Импортируем созданное нами представление
from .views import PostList,PostDetail,NewsCreate,NewsUpdate,NewsDelete #,create_product
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('News_all', PostList.as_view(), name='news_list'),
    path('News_all/<int:id>', PostDetail.as_view(), name= 'news_or_art_detail'),
    path('create_news/', NewsCreate.as_view(), name= 'create_news'),
    path('art/create_news/', NewsCreate.as_view(), name= 'create_art'),
    path('news_or_art/update/<int:pk>/', NewsUpdate.as_view(), name='news_update'),
    path('news_or_art/delete/<int:pk>/', NewsDelete.as_view(), name='news_delete')


]