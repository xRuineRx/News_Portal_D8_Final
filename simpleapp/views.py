from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import  News_All
from datetime import datetime
from .filters import  NewsFilter
from .forms import  NewsForm
from django.urls import reverse_lazy

# Create your views here.
class PostList(ListView):
    model = News_All
    ordering = '-time_in'

    template_name = 'flatpages/News_all.html'
    context_object_name = 'news'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = News_All
    pk_url_kwarg = 'id'

    template_name = 'flatpages/News_all_post.html'
    context_object_name = "news"

#Создание обновление и удаление новостей/статей

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_news_all',)
    form_class = NewsForm
    model = News_All
    template_name = 'flatpages/News_all_create_news.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news_or_art/art/create_news/':
            post.news_or_art = 'Ст'
        post.save()
        return super().form_valid(form)

class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_news_all',)
    form_class = NewsForm
    model = News_All
    template_name = 'flatpages/News_all_create_news.html'



class NewsDelete(DeleteView):
    model = News_All
    template_name = 'flatpages/news_delete.html'
    success_url = reverse_lazy('news_list')