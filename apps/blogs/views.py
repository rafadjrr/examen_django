from django.views.generic import ListView, DetailView,CreateView,TemplateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
from .models import *


class BlogListView(ListView):
    model = Blog
    template_name = "blogs/list.html"
    context_object_name = "blogs"
    paginate_by = 5
    
class AuthorListView(ListView):
    model = Author
    template_name = "author/list.html"
    context_object_name = "author"
    paginate_by = 5
    ordering = '-id'

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/detail.html"

class AuthorDetailView(DetailView):
    model = Author
    template_name = "author/detail.html"


class SuccessTemplateView(TemplateView):
    template_name = "success.html"


class BlogCreateView(CreateView):
    model = Blog
    template_name = "blogs/create.html"
    fields = ("__all__")
    success_url = reverse_lazy("urls_blog:success")

class AuthorCreateView(CreateView):
    model = Author
    template_name = "author/create.html"
    fields = ("__all__")
    success_url = reverse_lazy("urls_blog:success")

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blogs/update.html"
    fields = ("__all__")
    success_url = reverse_lazy("urls_blog:success")
    def form_valid(self, form):
        return super().form_valid(form)
    def post(self, request, *args, **kwargs):
        return super(BlogUpdateView,self).post(request, *args, **kwargs)

class AuthorUpdateView(UpdateView):
    model = Author
    template_name = "author/update.html"
    fields = ("__all__")
    success_url = reverse_lazy("urls_blog:success")
    def form_valid(self, form):
        return super().form_valid(form)
    def post(self, request, *args, **kwargs):
        return super(AuthorUpdateView,self).post(request, *args, **kwargs)

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blogs/delete.html"
    success_url = reverse_lazy("urls_blog:success")
class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "author/delete.html"
    success_url = reverse_lazy("urls_blog:success")


class InicioView(TemplateView):
    template_name = "inicio.html"
    