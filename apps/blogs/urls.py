from django.urls import path
from . import views

app_name = "urls_blog"

urlpatterns = [

    path('',views.InicioView.as_view(),name='inicio'),
    path('success',views.InicioView.as_view(),name='success'),

    path('listar_blogs/',views.BlogListView.as_view(),name='blog_all'),
    path('listar_author/',views.AuthorListView.as_view(),name='author_all'),
    
    path('ver_blog/<pk>/',views.BlogDetailView.as_view(),name='blog_detail'),
    path('ver_author/<pk>/',views.AuthorDetailView.as_view(),name='author_detail'),
    
    path('crear_blog/',views.BlogCreateView.as_view(),name='blog_detail'),
    path('crear_author/',views.AuthorCreateView.as_view(),name='author_detail'),
    
    path('update_blog/<pk>/',views.BlogUpdateView.as_view(), name='blog_update'),
    path('update_author/<pk>/',views.AuthorUpdateView.as_view(), name='author_update'),
    
    path('delete_blog/<pk>/',views.BlogDeleteView.as_view(), name='blog_delete'),
    path('delete_author/<pk>/',views.AuthorDeleteView.as_view(), name='author_delete')
    
]
